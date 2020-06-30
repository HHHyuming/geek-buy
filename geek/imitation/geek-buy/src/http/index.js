import axios from "axios";

const baseURL = 'http://127.0.0.1';

const Service = axios.create({
    baseURL
});

export function request(config) {
    return Service(config)

}
