import axios from 'axios';

let Connection : any = axios.create({
    baseURL: "http://localhost:8081",
    timeout: 1000*6
});


export {Connection};
export default  Connection;