<template>
    <div class="root">
        <div class="switch-img">
            <ul>
                <li  v-for="(_, index) in switchMap" :key="index" :style="currentIndex === index ? 'background-color: green ' : '' ">
                </li>
            </ul>
            <img :src="switchMap[currentIndex].imgSrc" alt="" >
        </div>

        <div class="icon-list">
            <div v-for="(iconItem, index) in iconList" :key="index">
                <img :src="iconItem.imgSrc" alt="">
                <span>{{iconItem.text}}</span>
            </div>
        </div>


    </div>
</template>

<script>
    // import {getRotationChart} from "../../http/home";

    export default {

        name: "FlashSale",
        data(){
            return{
                currentIndex:0,
                switchMap:[
                    {
                        imgSrc:"https:\/\/img.ddimg.mobi\/0ec4a32cbd84b1575892960355.jpg"
                    },
                    {
                        imgSrc: "https:\/\/img.ddimg.mobi\/d3d83d40395221575808767181.jpg"
                    },
                    {
                        imgSrc:  "https:\/\/img.ddimg.mobi\/1bb411f2cd09d1575815053778.jpg"
                    },
                    {
                        imgSrc:"https:\/\/img.ddimg.mobi\/b7efb94de888d1575820057576.jpg"


                    },{
                    imgSrc: "https:\/\/img.ddimg.mobi\/eb669d9799b8f1575907727553.jpg"
                    },
                    {
                        imgSrc:"https:\/\/img.ddimg.mobi\/168bff87979f11575943593312.jpg"
                    }
                ],
                iconList:[
                    {
                        imgSrc: require("images/icon/transport.png"),
                        text: "最快29分钟内送达"
                    },
                    {
                        imgSrc: require("images/icon/money.png"),
                        text: "0元起送 0元配送"
                    },
                    {
                        imgSrc: require("images/icon/seal.png"),
                        text: "安心退"
                    },

                ]
            }
        },
        methods:{
          setRotationChartSrc(){
              setInterval( () =>{
                if (this.currentIndex > 4){
                    this.currentIndex = 0
                }
                else{
                    this.currentIndex += 1
                }
              },1000)
          }
        },
        created() {
            this.setRotationChartSrc()
        }
    };
</script>

<style scoped>
    .root{
        padding: 0.3rem;
        /*position: relative;*/


    }
    .switch-img{
        height: 10rem;
        overflow: hidden;
        position: relative;
    }
    .switch-img img{
        height: 10rem;
        transition: 0.5s;
    }

    .switch-img ul{
        position: absolute;
        display: flex;
        bottom: 1.5rem;
        left: 40%;


    }
    .switch-img ul  > li{
        border: 1px solid green;
        width: 0.2rem;
        height: 0.2rem;
        margin-left: 0.2rem;
    }
    .icon-list{
        display: flex;
        justify-content: space-evenly;
        margin-top: 0.3rem;

    }
    .icon-list img{
        width: 0.8rem;

    }
    .icon-list  span{
        font-size: 0.2rem;
        margin-left: 0.3rem;
        color: greenyellow;

    }
    .icon-list > div{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .poster{
        margin-top: 0.3rem;
    }


</style>