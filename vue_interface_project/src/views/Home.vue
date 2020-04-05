<template>
  <div class="home">
      <div class="left-menu">
          <el-menu style="height: 100%"
            :default-active="activeIndex"
            class="el-menu-vertical-demo"
            background-color="#304156"
            text-color="#fff"
            @select="handleSelect"
            active-text-color="#409eff">

            <el-menu-item index="service" style="text-align: left">
              <i class="el-icon-menu"></i>
              <span slot="title">服务</span>
            </el-menu-item>
            <el-menu-item index="task" style="text-align: left">
              <i class="el-icon-setting"></i>
              <span slot="title">任务</span>
            </el-menu-item>
            <!-- <el-menu-item index="logout" style="text-align: left">
              <i class="el-icon-s-fold"></i>
              <span slot="title">退出登录</span>
            </el-menu-item> -->
        </el-menu>
      </div>
      <div class="right-context"> 
        <!-- 顶部的退出栏 -->
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

         <!-- 中间的板块内容，是根据左侧菜单栏变化的，这里用<router-view/>占个坑 -->
        <router-view/>
      
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
    import {logout, getLoginUserInfo} from "../request/user";

    export default {
      name: 'Home',
      components: {},
      props:{
        menu: String
      },
      data(){
         return{
           user: "",
           activeIndex: "service"
         }
      },
      methods: {
        handleSelect(index) {
          //将当前选择的模块的index赋值给activeIndex，因为发现:default-active好像是不会动态改变的，所以在这里需要重新赋值一次
          this.activeIndex = index  
           switch(index){
             case "service":
               console.log("选择的是service模块");
               this.$router.push('/service');
               break;
             case "task":
               console.log("选择的是task模块");
               this.$router.push('/task');
               break;  

           }
        },
        handleLogout(){
          logout().then(data=>{
             let success = data.data.success
             if (success){
               this.$router.push('/login')
             }else{
               this.$notify.error({
                          title: '错误',
                          message: '请求失败'
                      });
             }
          });
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
        this.activeIndex = this.menu;
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
