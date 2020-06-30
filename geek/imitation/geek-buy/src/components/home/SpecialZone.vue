<template>
    <div class="special-zone">
        <div class="special-title">特色专区
            <span class="timer-number">{{hour}}</span>
            <span class="timer-number">{{minute}}</span>
            <span class="timer-number">{{second}}</span>
            <span >更多></span>
        </div>

        <div class="special-content">
            <div v-for="(item,index) in product_list" :key="index">
                <div>
                <img :src="item.small_image" alt="">
                <span style="font-size: 0.5rem;">{{item.product_name}}</span>
                </div>
                <div class="special-price">
                    <div>
                    <span style="color: red">{{item.price | addPriceSymbol}}</span>
                    <span style="font-size: 0.6rem;"><del>{{item.origin_price}}</del></span>
                    </div>
                    <div>
                        <i class="iconfont icon-gouwucheman cart-font" ></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: "SpecialZone",
        data(){
            return{
                product_list:
                    [
                        {
                        "product_name": "爱森五花肉 500g",
                        "origin_price": "46.90",
                        "price": "41.80",
                        "spec": "高端五花肉 吃出幸福的滋味",
                        "small_image": "https://img.ddimg.mobi/product/4513b9fc5935f1548406258985.jpg!deliver.product.list",
                    },
                        {
                            "product_name": "粮全其美葱香味手抓饼 900g/袋",
                            "origin_price": "20.80",
                            "price": "18.80",
                            "small_image": "https://ddimg.ddxq.mobi/becc0e6b257781528108118451.jpg!maicai.product.list",
                        }, {
                        "product_name": "松花菜半颗 约500g",
                        "origin_price": "8.50",
                        "price": "7.59",
                        "small_image": "https://ddimg.ddxq.mobi/47a79cef49d661492078512642.jpeg!maicai.product.list",
                    }, {
                        "product_name": "美国车厘子 250g",
                        "origin_price": "32.90",
                        "price": "25.90",
                        "small_image": "https://img.ddimg.mobi/product/b960de0ed28d11562551037392.jpg!deliver.product.list",
                    },
                        {
                            "product_name": "芸豆 300g",
                            "origin_price": "9.90",
                            "price": "5.99",
                            "small_image": "https://img.ddimg.mobi/product/73c7833c39d6d1545274259948.jpg!maicai.product.list",
                        }, {
                        "product_name": "四季宝柔滑花生酱 340g/瓶",
                        "origin_price": "19.90",
                        "price": "16.90",
                        "small_image": "https://ddimg.ddxq.mobi/abf3023fb51611526109391551.jpg!maicai.product.list",
                    }, {
                        "product_name": "艺杏小油豆腐 130g/袋",
                        "origin_price": "4.90",
                        "price": "4.29",
                        "small_image": "https://img.ddimg.mobi/product/e0f55322f48ae1543472645397.jpg!maicai.product.list",
                    },
                        {
                            "product_name": "农夫山泉饮用天然水 550ml*28瓶",
                            "origin_price": "35.80",
                            "price": "32.80",
                            "small_image": "https://img.ddimg.mobi/product/9f71a4750f1591554301429547.jpg!deliver.product.list",
                        },
                        {

                            "product_name": "伊赛澳洲原切冷冻牛腱 1kg",
                            "origin_price": "79.90",
                            "price": "69.90",
                            "small_image": "https://img.ddimg.mobi/product/718558731a1eb1562568919636.jpg!deliver.product.list",

                        }, {
                        "product_name": "妙可蓝多马苏里拉奶酪碎 125g/袋",
                        "origin_price": "11.90",
                        "price": "8.90",
                        "small_image": "https://ddimg.ddxq.mobi/cedd7697d12571533723350035.jpg!maicai.product.list",
                    }, {
                        "product_name": "加费尔德舟山冷冻去脏小黄鱼 300g",
                        "origin_price": "18.80",
                        "price": "15.80",
                        "small_image": "https://img.ddimg.mobi/product/d9df7fe10be381548472525847.jpg!deliver.product.list",
                    }
                    ],
                hour:1,
                minute:21,
                second:1,
            }
        },
        filters:{
            addPriceSymbol(str){
                return  '￥' + str
            }
        }
    };
</script>

<style scoped>
.special-zone{
    background-color: white;
}
.special-title{
    border-left: 0.2rem solid yellowgreen;
    margin-left: 0.4rem;
    padding: 0.4rem;
    font-size: 0.8rem;
    position: relative;

}
.special-title > span:nth-child(-n+3){
    background-color: black;
    color: white;
    padding: 0.2rem;
    margin-left: 0.2rem;
    font-size: 0.5rem;
}
.special-title > span:last-child{
    position: absolute;
    right: 0;
    color: yellowgreen;
}
.special-content{
    display: flex;
    overflow-y: hidden;
    overflow-x: scroll;
    scroll-behavior: smooth;

}
.special-content::-webkit-scrollbar{
    display: none;
}

.special-content > div{
    width: 4rem;
    padding: 0.2rem 0.4rem;
    font-size: 0.7rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;


}
    .special-content img{
        width: 4rem;
    }
    .special-price{
        margin-top: 0.3rem;
        display: flex;
        justify-content: space-between;
    }
.special-price >div:nth-child(1){
    display: flex;
    flex-direction: column;
}

    .cart-font{
        color: yellowgreen;
        font-size: 0.9rem;
    }
</style>