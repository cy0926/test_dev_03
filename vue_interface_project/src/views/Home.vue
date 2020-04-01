<template>
  <div class="home">
      <div class="left-menu">
          <el-menu style="height: 100%"
            default-active="1"
            class="el-menu-vertical-demo"
            background-color="#304156"
            text-color="#fff"
            active-text-color="#409eff">

            <el-menu-item index="1" style="text-align: left">
              <i class="el-icon-menu"></i>
              <span slot="title">服务</span>
            </el-menu-item>
            <el-menu-item index="2" style="text-align: left">
              <i class="el-icon-setting"></i>
              <span slot="title">任务</span>
            </el-menu-item>
            <!-- <el-menu-item index="3" style="text-align: left">
              <i class="el-icon-s-fold"></i>
              <span slot="title" @click="handleLogout">退出登录</span>
            </el-menu-item> -->
        </el-menu>
      </div>
      <div class="right-context"> 
        <el-container>
            <el-header style="text-align: right; font-size: 16px"> 
              <el-dropdown>
                <i class="el-icon-setting" style="margin-right: 15px"></i>
                <el-dropdown-menu slot="dropdown">
                  <span @click="handleLogout">
                    <el-dropdown-item>退出</el-dropdown-item>
                  </span>
                </el-dropdown-menu>
              </el-dropdown>
              <span>{{user}}</span>
            </el-header>
        
            <el-main>
              <el-table>
                <el-table-column prop="date" label="日期" width="140">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="120">
                </el-table-column>
                <el-table-column prop="address" label="地址">
                </el-table-column>
              </el-table>
            </el-main>
        </el-container>
      
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
    import {logout, getLoginUserInfo} from "../request/user";

    export default {
      name: 'Home',
      components: {},
      data(){
         return{
           user: ""
         }
      },
      methods: {
        handleLogout(){
          logout().then(data=>{
             let success = data.data.success
             if (success){
               this.$router.push('/login')
             }
          })
        }
      },
      created(){
        getLoginUserInfo().then(data=>{
            let success = data.data.success
            if (success){
               this.user = data.data.data.name;
               console.log("登录用户是：", this.user)
            }else{
              this.$router.push('/')
            }
        });
      }
    }

</script>

<style scoped>
    .home {
      display: flex;
      height: 100%;
    }
    .left-menu {
      width: 15%;
    }
    .right-context {
      width: 85%;
    }
</style>
