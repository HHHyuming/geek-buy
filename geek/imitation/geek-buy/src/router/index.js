import VueRouter from "vue-router";
import Vue from 'vue'

Vue.use(VueRouter)
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

const routes = [
    {
        path:'/',
        redirect:'/home'
    },
    {
        path: '/home',
        name:'home',
        component: () =>import('../components/home/MainPage'),


    },
    {
        path:'/cart',
        component:() => import('../components/cart/MainCart'),
        name:'cart'
    },
    {
        path:'/category',
        component:() => import('../components/category/MainCategory'),
        name:'category'
    },
    {
        path:'/eat',
        component: () => import('../components/eat/MainEat'),
        name:'eat'
    },
    {
        path: '/profile',
        component: () => import('../components/profile/MainProfile'),
        name:'profile'
    },
    {
        path:'/map',
        component:() =>import('../components/home/Map'),
        name:'map',
    },{
    path:'/userAction',
        component:() => import('../components/user/LoginAndRegister'),
        name: 'userAction'
    }

];

const router = new VueRouter({
    routes
});

export default router