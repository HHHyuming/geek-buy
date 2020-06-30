<template>
    <div style="position: relative">
    <div class="TabMenu">
        <TabItem class="tabItem" v-for="(item,index) in recommendData" :key="index" @click.native="changeIndex(index)">
                <img  :src="currentIndex===index? item.active : item.default" slot="icon">
                <span slot="text-content" :class="currentIndex===index ? 'activeFontColor' : ''">{{item.text}}</span>

        </TabItem>

    </div>
    </div>
</template>

<script>
    import TabItem from "./common/TabItem";
    export default {
        name: "TabMenu",
        components:{
            TabItem
        },
        data(){
            return{
                currentIndex:0,
                // 导航 icon
                recommendData:[
                    {
                        active:require("../images/tabbar/home_selected.png"),
                        default:require("../images/tabbar/home_default.png"),
                        text:'首页',
                        url_path:'home'
                    },
                    {
                        active:require("../images/tabbar/category_selected.png"),
                        default:require("../images/tabbar/category_default.png"),
                        text:'分类',
                        url_path:'category'
                    },
                    {
                        active:require("../images/tabbar/eat_selected.png"),
                        default:require("../images/tabbar/eat_default.png"),
                        text:'吃什么',
                        url_path:'eat'
                    },
                    {
                        active:require("../images/tabbar/shoppingcart_selected.png"),
                        default:require("../images/tabbar/shoppingcart_default.png"),
                        text: '购物车',
                        url_path:'cart'
                    },
                    {
                        active:require("../images/tabbar/mine_selected.png"),
                        default:require("../images/tabbar/mine_default.png"),
                        text: '我的',
                        url_path:'profile'
                    }
                ]
            }
        },
        methods:{
            changeIndex(index){
                this.currentIndex = index;
                this.$router.push({name:this.recommendData[index].url_path})
            }
        },
        computed:{

        }
    };
</script>

<style scoped>
    .TabMenu{
        position: fixed;
        bottom: 0;
        background-color: white;
        padding-top: 0.3rem;
        z-index: 2;
        height: 2.5rem;
        display: flex;
        width: 100%;
        box-sizing: border-box;


    }

.tabItem{
    flex: 1;
}


    .activeFontColor{
        color: green;
    }
</style>