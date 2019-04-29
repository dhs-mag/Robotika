<template>
    <div class="control text-center">
        <div class="row mx-0">
            <div class="col-4 offset-4 px-0 border-left border-right border-top" @click="moveForward">
                <span>👆</span>
            </div>
        </div>
        <div class="row mx-0 border-top">
            <div class="col-4 px-0" @click="moveLeft">
                <span>👈</span>
            </div>
            <div class="col-4 px-0 border-left border-right" @click="moveBack">
                <span>👇</span>
            </div>
            <div class="col-4 px-0" @click="moveRight">
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
    }
</script>

<style scoped lang="scss">
    .control {
        > .row{

            > *{
                cursor: pointer;
                background: #c6c8ca;
            }

            span{
                font-size: 6rem;
                line-height: 20vh;
            }
        }
    }
</style>
