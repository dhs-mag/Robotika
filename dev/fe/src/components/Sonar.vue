<template>
    <div class="sonar">

        <template v-if="serverData.status === 'ok'">
            <div class="row mt-5">
                <div class="col-4 offset-4">
                    <div class="d-flex justify-content-between">
                        <div
                                v-for="(segmentDistance, it) in serverData.sonar.distance"
                                class="segment-wrap"
                                :style="{transform: 'rotate('+getDegrees(it)+'deg)'}"
                        >
                            <span :style="{bottom: getPercent(segmentDistance)}">{{segmentDistance}}</span>
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
        public maxDistance: number;

        static MAX_DISTANCE = 100;

        constructor() {
            super();

            this.maxDistance = Sonar.MAX_DISTANCE;

            this.serverData = {
                status: 'not connected to server',
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
            } catch (e) {
                console.log(e);
            }
        }
    }
</script>

<style scoped lang="scss">
    .segment-wrap {
        width: 3px;
        height: 60vh;
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
</style>
