import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Producer from '@/components/Producer'
import Retailer from '@/components/Retailer'
import Consumer from '@/components/Consumer'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Hello',
            component: Hello
        },
        {
            path: '/producer',
            name: 'Producer',
            component: Producer
        },
        {
            path: '/retailer',
            name: 'Retailer',
            component: Retailer
        },
        {
            path: '/consumer',
            name: 'Consumer',
            component: Consumer
        }
    ],
    mode: 'history'
})
