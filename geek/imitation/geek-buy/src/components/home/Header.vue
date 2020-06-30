<template>
    <div class="root">
        <div class="location" @click="showMap">
            <i class="iconfont icon-location"></i>
            定位信息
            <i class="iconfont icon-xiala2"></i>
        </div>
        <div class="search-goods">
            <i class="iconfont icon-search"></i>
            <label for="search-input" style="margin-left: 0.3rem">
                <input id="search-input" type="text" v-model="queryArg" placeholder="请输入商品名称">
            </label>

        </div>
    </div>
</template>

<script>

    export default {
        name: "Header",
        components:{
        },
        data(){
            return{
                queryArg:'',
            }
        },
        methods:{
            showMap(){
                this.$router.push({path:'/map'})
            }
        }
    };
</script>

<style scoped>
    .root{
        font-size: .6rem;
        display: flex;
    }
.location{
    border-radius: 1rem;
    background-color: orange;
    padding: .3rem;
    color: white;

}
.search-goods{
    border-radius: 1rem;
    background-color: white;
    border: 1px solid red;
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ccc;

}
    .search-goods input{
        outline: none;
        border: none;
    }
    .search-goods input::placeholder{
        /*outline: none;*/
        /*border: none;*/
        color: #bbb;
        font-size: 0.6rem;
        letter-spacing: 0.1rem;
    }
</style>