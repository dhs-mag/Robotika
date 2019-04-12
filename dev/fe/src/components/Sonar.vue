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
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import {Connection} from '../../lib/Connection';

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


        getSonarData(){
            Connection.get("/api/sonar").then((response : APIResponseI) =>{
               this.serverData = response.data;
            });
        }
    }
</script>

<style scoped lang="scss">

</style>
