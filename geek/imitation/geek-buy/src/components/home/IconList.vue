<template>
    <div class="icon-list">
        <IconItem v-for="(iconItem,index) in icon_list"  :key="index">
            <img :src="iconItem.icon_url" alt="" slot="icon">
            <span slot="text-content">{{iconItem.name}}</span>
        </IconItem>
    </div>
</template>

<script>
    import IconItem from "./IconItem";
    export default {
        name: "IconList",
        components:{
            IconItem
        },
        data(){
            return{
                "icon_list": [{
                    "icon_url": "https://img.ddimg.mobi/faed0c89b1ac61561979943620.jpg",
                    "name": "安心蔬菜"
                }, {
                    "icon_url": "https://img.ddimg.mobi/a79822f496ec71561980537120.jpg",
                    "name": "豆制品"
                }, {
                    "icon_url": "https://img.ddimg.mobi/febc9219e5f061561980283162.jpg",
                    "name": "水果"
                }, {
                    "icon_url": "https://img.ddimg.mobi/57742da7f00ab1562725189267.jpg",
                    "name": "肉禽蛋"
                }, {
                    "icon_url": "https://img.ddimg.mobi/3f96191b097cd1562204510108.jpg",
                    "name": "海鲜水产"
                }, {
                    "icon_url": "https://img.ddimg.mobi/a19a8501bf4041561980956934.jpg",
                    "name": "乳品烘焙"
                }, {
                    "icon_url": "https://img.ddimg.mobi/baf53e7d1e9ce1561980371874.jpg",
                    "name": "营养早餐"
                }, {
                    "icon_url": "https://img.ddimg.mobi/cc39ecee3cee51564386403745.jpg",
                    "name": "叮咚心选"
                }, {
                    "icon_url": "https://img.ddimg.mobi/67260446df1451561980456552.jpg",
                    "name": "米面粮油"
                }, {
                    "icon_url": "https://img.ddimg.mobi/17964fae5012d1561980650167.jpg",
                    "name": "调味品"
                }]
            }
        }
    };
</script>

<style scoped>
.icon-list{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    background-color: white;
    width: 100%;
}
    .icon-list > div{
        flex: 1;
    }
</style>