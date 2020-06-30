import {request} from './index'

export function getRotationChart() {
    return request({
        method:'get',
    })
}