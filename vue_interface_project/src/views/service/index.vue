<template>
    <div class="service-main">
          <el-button @click="openAddModel">创建服务</el-button>

          <!-- 点击创建服务之后的dialog弹出框 -->
          <el-dialog 
            title="创建服务" 
            :visible.sync="dialogAddVisible" 
            width="30%"
            @close="resetAddForm('addFormRef')"
          >
            <el-form :model="addForm" :rules="addRules" ref="addFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                  <el-input v-model="addForm.name"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                  <el-input v-model="addForm.description" type="textarea"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
              <el-button  @click= "dialogAddVisible= false">取 消</el-button>
              <el-button type="primary" @click="addServiceFun">确 定</el-button>
            </span>
          </el-dialog>

          <!-- 点击单个服务的编辑之后的dialog弹出框 -->
          <el-dialog 
            title="编辑服务" 
            :visible.sync="dialogEditVisible" 
            width="30%"
            @close="resetEditForm('editFormRef')"
          >
            <el-form :model="editForm" :rules="editRules" ref="editFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                  <el-input v-model="editForm.name"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                  <el-input v-model="editForm.description" type="textarea"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
              <el-button  @click= "dialogEditVisible= false">取 消</el-button>
              <el-button type="primary" @click="EditServiceFun">确 定</el-button>
            </span>
          </el-dialog>

          <!-- service列表 -->
          <div class="service-list">
              <el-card class="service-card" v-for="item in serviceList" :key="item.id">
                  <div slot="header" class="service-card-header">
                    <div>
                        {{item.name}}
                    </div>
                    <div>
                        <el-button 
                        style="padding: 3px 0"  type="text"
                        @click="openEditModel(item)">编辑
                        </el-button>
                        <el-button 
                        style="padding: 3px 0"  type="text"
                        @click="deleteServiceFun(item)">删除
                        </el-button>

                    </div>                    
                  </div>

                  <div>
                    {{item.description}}
                  </div>            
              </el-card>
            
          </div>

    </div>

</template>

<script>

import { addService, getAllServices, updateService, deleteService} from "../../request/service";

export default {
      name: "index",
      data(){
        return {
            dialogAddVisible: false,
            dialogEditVisible: false,
            addForm: {
              name:"",
              description: ""              
            },
            addRules: {
              name: [
                { required: true, message: '请输入服务名称', trigger: 'blur' },
              ],
              description: [
                { required: true, message: '请输入服务描述', trigger: 'change' }
              ],
            },
            editForm: {
              id: 0,
              name: "",
              description: ""
            },
            editRules: {
              name: [
                { required: true, message: '请输入服务名称', trigger: 'blur' },
              ],
              description: [
                { required: true, message: '请输入服务描述', trigger: 'change' }
              ],
            },
            serviceList: [],
        }
      },
      methods: {
        openAddModel(){    //打开创建服务的窗口
           this.dialogAddVisible = true;
        },
        openEditModel(data) {  //打开编辑服务的窗口
           this.dialogEditVisible = true;
           this.editForm.id = data.id;
           this.editForm.name = data.name;
           this.editForm.description = data.description;
           
        },
        getAllServicesFun(){  //这是获取所有服务列表的方法
           getAllServices().then(data=>{
                let success = data.data.success
                if (success){
                    this.serviceList = data.data.data;
                }else{
                  this.$notify.error({
                         title: '错误',
                         message: '请求失败'
                   });
                }

           })
        },
        addServiceFun(){   //这是请求创建服务
           this.$refs.addFormRef.validate((valid) => {
              if (valid) {
                  // 表单必填项校验通过
                  addService(this.addForm).then(data=>{
                    let success = data.data.success
                    if(success){
                       this.dialogAddVisible = false;
                       this.getAllServicesFun();
                       
                    }else {
                      this.$notify.error({
                         title: '错误',
                         message: '请求失败'
                      });
                    }
                  })
              } else {
                return false;
              }
            });            
        },
        EditServiceFun(){  //这是请求编辑服务
           this.$refs.editFormRef.validate((valid) => {
              if (valid) {
                 // 表单必填项校验通过
                 updateService(this.editForm.id, this.editForm).then(data=>{
                     let success = data.data.success
                     if (success) {
                        this.dialogEditVisible = false;
                        this.getAllServicesFun();
                     }else {
                         this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                         });
                     }
                 });
              } else {
                return false;
              }
           });
        },
        deleteServiceFun(data){
            this.$confirm(`是否确定要删除: ${data.name}`,'警告', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              dangerouslyUseHTMLString: true,
              type: 'warning'
            }).then(() => {
              deleteService(data.id).then(data=>{
                  let success = data.data.success
                  if (success){
                    this.getAllServicesFun();
                  }else {
                    this.$notify.error({
                          title: '错误',
                          message: '请求失败'
                    });                    
                  }
                });              
            }).catch(() => {
              //点击取消，就什么都不做
            });

        },
        resetAddForm(formName) {  // 对整个表单进行重置，将所有字段值重置为初始值并移除校验结果
            this.$refs[formName].resetFields();
        },
        resetEditForm(formName){  // 对整个表单进行重置，将所有字段值重置为初始值并移除校验结果
            this.$refs[formName].resetFields();
        }
      },
      created() {
            this.getAllServicesFun();
      }
  
}
</script>

<!--这里是重写element的css， 不能有scoped属性，所以这里是全局的-->
<style>
    .el-card__header {
        padding: 10px 20px;
        border-bottom: 1px solid #EBEEF5;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }
</style>

<style scoped>
   .service-main {
      text-align: left;
      padding: 5px 5px;
   }
   .service-list {
      display: flex;
      flex-wrap: wrap;
   }
  .service-card {
    width: 300px;
    margin-top: 5px;
    margin-right: 10px;
   }
  .service-card-header {
      display: flex;
      justify-content: space-between;
  }

</style>