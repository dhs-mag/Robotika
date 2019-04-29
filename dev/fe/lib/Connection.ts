import axios from 'axios';

let Connection : any = axios.create({
    baseURL: "/",
    timeout: 1000*6
});


export {Connection};
export default  Connection;