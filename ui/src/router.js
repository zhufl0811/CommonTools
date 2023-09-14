// import Vue from 'vue'
// //1.导⼊
// import Router from 'vue-router'
import {createRouter, createWebHistory} from 'vue-router'
import Login from './views/Login.vue'
import YoloModel from './views/model.vue'
import LayoutView from './layout/index'
 
const routerHistory = createWebHistory()
 
const router = createRouter({
    history: routerHistory,
    routes:[
        {
            path:'/',
            component:LayoutView,
            name:'home',
            redirect:'/login',
            children:[
                {
                    path: '/login',
                    name:'login',
                    component: Login
                },
                {
                    path: '/model',
                    name:'model',
                    component: YoloModel
                }
            ]
        }    
    ]
})

export default router