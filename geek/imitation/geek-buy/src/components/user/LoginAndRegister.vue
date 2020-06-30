<template>
    <div class="root">
        <div>
            <div>
                <span>登录</span>
                <span>注册</span>
            </div>
            <div>
                <div class="phone-login">
                    <div v-show="phoneLogin">
                        <div>
                            <label for="phoneNum">
                                手机号
                                <input type="text" id="phoneNum" required placeholder="请输入手机号码">
                            </label>
                        </div>
                        <div>
                            <label for="verifyCode">
                                请输入验证码
                                <input type="text" id="verifyCode" required placeholder="请输入验证码">
                                <button>发送验证码</button>
                            </label>
                        </div>
                        <div>
                            <button></button>
                        </div>
                        <div>
                            <span @click="phoneLogin=false">账号密码登录</span>
                        </div>
                    </div>

                    <div v-show="!phoneLogin">
                        <div>
                            <label for="phoneNum">
                                手机号
                                <input type="text" id="phoneNum2" required placeholder="请输入手机号码">
                            </label>
                        </div>
                        <div>
                            <label for="password">
                                手机号
                                <input type="text" id="password" required placeholder="请输入密码">
                            </label>
                        </div>
                        <div>
                            <label for="verifyCode">
                                请输入验证码
                                <input type="text" id="verifyCode2" required placeholder="请输入验证码">
                                <button>发送验证码</button>
                            </label>
                        </div>
                        <div>
                            <button></button>
                        </div>
                    </div>
                </div>
                <div class="register">
                    <div>
                        <div>
                            <label for="registerPhoneNum">
                                手机号码
                                <input type="text" id="registerPhoneNum" placeholder="请输入手机号码" required>
                            </label>
                        </div>

                        <div>
                            <label for="registerPassword">
                                密码
                                <input type="text" id="registerPassword" placeholder="请输入密码(不少于6位)" required>
                            </label>
                        </div>

                        <div>
                            <button>注册</button>
                        </div>
                    </div>
                </div>
            </div>

            <div>其他登录方式</div>

            <div>
                <div>wx</div>
                <div>qqq</div>
            </div>

            <div>
                温馨提示
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                phoneLogin:true,
            }
        },
        methods:{

        }
    };
</script>

<style scoped>
.root{
    background: url("../../../src/images/login/back2.jpg") no-repeat;
    background-size: 100% 100%;
    width: 100vw;
    height: 100vh;
}

.root > div:nth-child(1){
position: absolute;
background-color: #eee;
top: 10vh;
    bottom: 15vh;

}

input{
    border: none;
    outline: none;
}
    input::placeholder{
        color: #ccc;
    }
</style>