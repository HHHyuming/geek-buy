<template>
    <div>
        <div class="icon-item">
            <div class="iconStyle">
                <slot name="icon"></slot>
            </div>
            <div><slot name="text-content"></slot></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "IconItem",
        data(){
            return{
            }
        }
    };
</script>

<style scoped>
    .iconStyle{

    }
.iconStyle img{
    width: 2rem;

}
.icon-item{
display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 0.6rem;
    padding: 0.4rem;
    color: #aaa;
}



</style>