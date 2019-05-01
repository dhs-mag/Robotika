<template>
    <div class="sonar">

        <div v-show="serverData.status === 'ok'">
            <canvas id="chart-0"></canvas>
        </div>
        <div v-show="serverData.status !== 'ok'">
            <div class="text-center p-5">
                <h2>Something went wrong:</h2>
                <p><strong>Status:</strong> {{serverData.status}}</p>
            </div>
        </div>
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
        private chart: any = null;

        constructor() {
            super();

            this.maxDistance = Sonar.MAX_DISTANCE;

            this.serverData = {
                status: 'not connected to server',
                // status: 'ok',
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
                    animation:{
                        duration: 1000,
                        easing: 'easeOutQuad'
                    },
                    startAngle: Math.PI,
                    maintainAspectRatio: true,
                    aspectRatio: 1.7,
                      scale: {
                        ticks: {
                            min: 0,
                            max: 10
                        }
                      },
                    spanGaps: false,
                    elements: {
                        line: {
                            tension: 0.4
                        }
                    },
            }
            };



            setInterval(()=>{
                this.getSonarData();
            }, 500);
        }




        mounted() {



            // chart

            const context :any = document.getElementById("chart-0");

            this.chart = new Chart(context, this.config);


        }

        generateDataset(totalSegments: any){

            let output : any = [];

            for (let i: any = 0; i < totalSegments; i++){

                let arr =  new Array((totalSegments * 2) - 1).fill(0);

                arr.splice(i, 0, 0);

                output.push({
                        backgroundColor: "green",
                        borderColor: "white",
                        data: arr,
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
                    this.config.data.datasets = this.generateDataset(this.serverData.sonar.segments);
                }

                this.config.data.datasets.forEach((piece:any, i: number) => {

                    let value = Math.min((this.serverData.sonar.distance[i] / 10.0) * (10/8), 10);
                    let dataset = this.config.data.datasets[i];

                    dataset.data[i] = value;
                    if (value < 4){
                        dataset.backgroundColor = "red";
                    } else if (value < 5) {
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
        height: 100%;
        position: fixed;
        top: 0;
        bottom: 0;
        z-index: 9;
    }

</style>
