<template>
    <div class="root">
        <div class="BackImg">
            <Header class="header"></Header>
            <FlashSale></FlashSale>
        </div>
        <div class="poster">
            <img src="http://518taole.7-orange.cn/homead2.gif" alt="">
        </div>

        <IconList></IconList>
        <SpecialZone ></SpecialZone>
        <RenderData></RenderData>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
        <div>1</div>
    </div>
</template>

<script>
    import Header from "./Header";
    import FlashSale from "./FlashSale";
    import IconList from "./IconList";
    import SpecialZone from "./SpecialZone";
    import RenderData from "./RenderData";
    export default {
        name: "MainPage",
        components:{
            Header,
            FlashSale,
            IconList,
            SpecialZone,
            RenderData ,

        },
        methods:{
            initMap(){
                let mapObj = new AMap.Map('testMap', {//'map-location'是对应页面盒子的id
                    resizeEnable: true, //自适应大小
                    zoom: 10//初始视窗
                });
                AMap.plugin('AMap.Geolocation', function() {
                    var geolocation = new AMap.Geolocation({
                        // 是否使用高精度定位，默认：true
                        enableHighAccuracy: true,
                        // 设置定位超时时间，默认：无穷大
                        // timeout: 10000,
                        // 定位按钮的停靠位置的偏移量，默认：Pixel(10, 20)
                        buttonOffset: new AMap.Pixel(10, 20),
                        //  定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
                        zoomToAccuracy: true,
                        //  定位按钮的排放位置,  RB表示右下
                        buttonPosition: 'RB'
                    })

                    geolocation.getCurrentPosition()
                    AMap.event.addListener(geolocation, 'complete', onComplete)
                    AMap.event.addListener(geolocation, 'error', onError)

                    function onComplete (data) {
                        // data是具体的定位信息
                        console.log('定位');
                        console.log(data);
                    }

                    function onError (data) {
                        // 定位出错
                        console.log('error');
                        console.log(data);
                    }
                })
            }
        },
        mounted() {
            this.initMap()
        }
    };
</script>


<style scoped>
    .BackImg{
        padding-top: 0.3rem;

        background-image: url("../../../src/images/home/backImage.png");

    }

#testMap{
    width: 20rem;
    height: 15rem;
    border: 1px solid blue;
}

.poster{
    margin-bottom: -0.1rem;
}
    .poster img{
        width: 100%;

    }
</style>