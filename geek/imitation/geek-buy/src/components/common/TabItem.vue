<template>
    <div class="tabItem">
        <div>
            <div class="iconClass"><slot name="icon" ></slot></div>

            <div><slot name="text-content"></slot></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TabItem",
        props:{
            iconClass:{
                type:Object,
                default(){
                    return {}
                },
            }
        },
        data(){
            return{

            }
        }

    };
</script>

<style scoped>
.tabItem >div{
    display: flex;
    flex-direction: column;
    font-size: .5rem;
    align-items: center;

}

.tabItem img{
    width: .9rem;
}


.iconClass{
    margin-bottom: 0.3rem ;
}


</style>