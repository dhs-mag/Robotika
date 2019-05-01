<template>
    <div class="sonar">

        <template v-if="serverData.status === 'ok'">
            <canvas id="chart-0"></canvas>
            <div class="row pt-5 pb-3">
                <div class="col-4 offset-4">


                    <div class="d-flex justify-content-between">
                        <div
                                v-for="(segmentDistance, it) in serverData.sonar.distance"
                                class="segment-wrap"
                                :style="{transform: 'rotate('+getDegrees(it)+'deg)'}"
                        >
                            <span :style="{bottom: getPercent(segmentDistance)}">{{Math.round(segmentDistance)/10}}cm</span>
                        </div>
                    </div>
                </div>
            </div>
        </template>
        <template v-else>
            <div class="text-center p-5">
                <h2>Something went wrong:</h2>
                <p><strong>Status:</strong> {{serverData.status}}</p>
            </div>
        </template>
    </div>
</template>


<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    import {Connection} from '../../lib/Connection';
    import Chart from 'chart.js';

    interface SonarI{
        serverData : ServerDataI;
    }

    interface ServerDataI{
        status: string;
        sonar: ServerDateSonarI
    }

    interface ServerDateSonarI{
        segments: number,
        viewAngle: number,
        distance: Array<number>
    }

    interface APIResponseI{
        data: ServerDataI
    }

    @Component
    export default class Sonar extends Vue implements SonarI {
        public serverData: ServerDataI;
        public maxDistance: number;

        public config: any;

        static MAX_DISTANCE = 100;
        private chart: Chart;

        constructor() {
            super();

            this.maxDistance = Sonar.MAX_DISTANCE;

            this.serverData = {
                // status: 'not connected to server',
                status: 'ok',
                sonar: {
                    distance: [45,
                                39.75,
                                54.33333333,
                                37,
                                51.75,
                                31.5,
                                53.6,
                                ],
                    segments: 7,
                    viewAngle: 140
                }
            };


            this.config= {
                type: 'polarArea',
                data: {
                    datasets: []
                },
                options: {
                startAngle: Math.PI,
                maintainAspectRatio: true,
                spanGaps: false,
                elements: {
                    line: {
                        tension: 0.4
                    }
                },
                plugins: {
                    filler: {
                        propagate: false
                    },
                    'samples-filler-analyser': {
                        target: 'chart-analyser'
                    }
                }
            }
            };



            setInterval(()=>{
                this.getSonarData();
            }, 500);
        }




        mounted() {



            // chart

            const context = document.getElementById("chart-0");

            this.chart = new Chart(context, this.config);


        }

        generateDataset(totalSegments){

            let output = [];

            for (let i = 0; i < totalSegments; i++){

                output.push({
                        backgroundColor: "green",
                        borderColor: "white",
                        data: new Array((totalSegments * 2) - 1).fill(0).splice(i, 0, 0),
                    });
            }

            return output;

        }

        getDegrees(it : number) : number{
            let {segments, viewAngle} = this.serverData.sonar;

            var segmentDeg = viewAngle / segments;

            return ((viewAngle - segmentDeg) / -2) + (segmentDeg * it);
        }

        getPercent(val : number) : string{
            return ((val / Sonar.MAX_DISTANCE) * 100) + '%';
        }

        async getSonarData() : Promise<void> {

            try{
                let response = await  Connection.get("/api/sonar");
                this.serverData = response.data;

                if (this.config.data.datasets.length != this.serverData.sonar.segments){
                    this.generateDataset(this.serverData.sonar.segments);
                }

                this.config.data.datasets.forEach((piece, i) => {

                    let value = this.serverData.sonar.segments[i] / 10;
                    let dataset = this.config.data.datasets[i];

                    dataset.data[i] = value;
                    if (value < 40){
                        dataset.backgroundColor = "red";
                    } else if (value < 50) {
                        dataset.backgroundColor = "orange";
                    } else {
                        dataset.backgroundColor = "green";
                    }
                });
                this.chart.update();


            } catch (e) {
                console.log(e);
            }
        }
    }




</script>

<style scoped lang="scss">
    .segment-wrap {
        width: 3px;
        height: 50vh;
        background: red;
        display: block;
        position: relative;
        transform-origin: bottom center;

        span {
            position: absolute;
            width: 120px;
            height: 3px;
            display: block;
            background: green;
            margin-left: -60px;
            top: auto;
            left: 1px;
        }
    }

    #chart-0 {
        width: 70%;
    }

</style>
