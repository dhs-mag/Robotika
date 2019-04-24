import axios from 'axios';

let Connection : any = axios.create({
    baseURL: "http://192.168.42.211:8081",
    timeout: 1000*6
});


export {Connection};
export default  Connection;