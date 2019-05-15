<template>
    <div class="control text-center">
        <div class="row mx-0">
             <div class="col-4 px-0 bg-success" v-touch:start="startAuto" @mousedown="startAuto">
                <span>👨‍✈️</span>
            </div>
            <div class="col-4 px-0 border-left border-right" v-touch:start="moveForward" @mousedown="moveForward" v-touch:end="stopAuto" @mouseup="stopAuto">
                <span>👆</span>
            </div>
            <div class="col-4 px-0 bg-danger" v-touch:start="stopAuto" @mousedown="stopAuto">
                <span>👷‍♀️</span>
            </div>
        </div>
        <div class="row mx-0 border-top">
            <div class="col-4 px-0" v-touch:start="moveLeft" @mousedown="moveLeft" v-touch:end="stopAuto" @mouseup="stopAuto">
                <span>👈</span>
            </div>
            <div class="col-4 px-0 border-left border-right" v-touch:start="moveBack" @mousedown="moveBack" v-touch:end="stopAuto" @mouseup="stopAuto">
                <span>👇</span>
            </div>
            <div class="col-4 px-0" v-touch:start="moveRight" @mousedown="moveRight" v-touch:end="stopAuto" @mouseup="stopAuto">
                <span>👉</span>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    import {Connection} from '../../lib/Connection';

    @Component
    export default class Control extends Vue{


        constructor() {
            super();
        }

        async moveForward(): Promise<void> {
            try {
                await Connection.get("/api/move/forward");
            } catch (e) {
                console.log(e);
            }
        }

        async moveLeft(): Promise<void> {
            try {
                await Connection.get("/api/move/left");
            } catch (e) {
                console.log(e);
            }
        }

        async moveBack(): Promise<void> {
            try {
                await Connection.get("/api/move/back");
            } catch (e) {
                console.log(e);
            }
        }

        async moveRight(): Promise<void> {
            try {
                await Connection.get("/api/move/right");
            } catch (e) {
                console.log(e);
            }
        }

        async startAuto(): Promise<void> {
            try {
                await Connection.get("/api/auto/start");
            } catch (e) {
                console.log(e);
            }
        }

        async stopAuto(): Promise<void> {
            try {
                await Connection.get("/api/auto/stop");
            } catch (e) {
                console.log(e);
            }
        }
    }
</script>

<style scoped lang="scss">
    .control {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 99;

        > .row{

            > *{
                cursor: pointer;
                background: #c6c8ca;
            }

            span{
                font-size: 5rem;
                line-height: 20vh;
            }
        }
    }
</style>
