<template>
    <div class="hello">
        <h1>my sonar template</h1>


        <template v-if="serverData.status === 'ok'">

            <p>
                <strong>Status</strong><br>
                {{serverData.status}}
            </p>
            <p>
                <strong>Segments</strong><br>
                {{serverData.sonar.segments}}
            </p>
            <p>
                <strong>Angle</strong><br>
                {{serverData.sonar.viewAngle}}
            </p>
            <p>
                <strong>Distance</strong><br>
                {{serverData.sonar.distance}}
            </p>

        </template>
        <div id="graph"></div>
    </div>
</template>

<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    import {Connection} from '../../lib/Connection';
    import * as Plotly from 'plotly.js';

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

        constructor() {
            super();

            this.serverData = {
                status: 'failed',
                sonar: {
                    distance: [0],
                    segments: 1,
                    viewAngle: 90
                }
            };
            setInterval(()=>{
                this.getSonarData();
            }, 500);
        }

        mounted() {
            /*var data : Plotly.BarData[] = [{
                type: "scatterpolargl",
                r: [50, 300, 900],
                theta: [0, 90, 180],
                subplot: "polar3"
            }];

            var layout = {
                polar3: {
                    domain: {
                        x: [0.54, 1],
                        y: [0.56, 1]
                    },
                    radialaxis: {
                        type: "log",
                        tickangle: 45
                    },
                    sector: [0, 180]
                },
                showlegend: false
            };


            Plotly.newPlot('graph', data, layout);*/
        }

        async getSonarData() : Promise<void> {

            try{
                let response = await  Connection.get("/api/sonar");
                console.log(response);
                this.serverData = response.data;
            } catch (e) {
                console.log(e);
            }
        }
    }
</script>

<style scoped lang="scss">

</style>
