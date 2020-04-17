<template>
    <div class="task-main"> 
        <el-button @click="openAddModel">创建任务</el-button>

        <!-- 点击创建服务之后的dialog弹框 -->
        <el-dialog
            title="创建服务"
            :visible.sync="dialogAddVisible"
            width="30%"
            @close="resetAddForm('addFormRef')">

            <!-- @submit.native.prevent：禁用回车 -->
            <el-form :model="addForm" :rules="addRules" ref="addFormRef" @submit.native.prevent
                label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="addForm.name"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                    <el-input v-model="addForm.description" type="textarea"></el-input>
                </el-form-item>
            </el-form>

            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogAddVisible = false">取 消</el-button>
                <el-button type="primary" @click="addTaskFun">确 定</el-button>
            </span>
        </el-dialog>

        <!-- 点击编辑服务之后的dialog弹框 -->
        <el-dialog
            title="编辑任务"
            :visible.sync="dialogEditVisible"
            width="30%"
            @close="resetEditForm('editFormRef')">

            <!-- @submit.native.prevent：禁用回车 -->
            <el-form :model="editForm" :rules="editRules" ref="editFormRef" @submit.native.prevent
                label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="editForm.name"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                    <el-input v-model="editForm.description" type="textarea"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogEditVisible = false">取 消</el-button>
                <el-button type="primary" @click="eidtTaskFun">确 定</el-button>
            </span>
        </el-dialog>

        <!-- Task列表 -->
        <div class="task-list">
            <el-card class="task-card" v-for="item in taskList" :key="item.id">
                <div slot="header" class="task-card-header">
                    <div>
                        <span>{{item.name}}</span>
                    </div>
                    <div>
                        <el-button style="padding: 3px 0" type="text" 
                        @click="openEditModel(item)">编辑</el-button>
                        <el-button style="padding: 3px 0" type="text"
                        @click="deleteTaskFun(item)">删除</el-button>
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
import {getAllTasks,addTask,updateTask,deleteTask} from "../../request/task";
export default {
    name: "index",
    data(){
        return {
            taskList: [],
            dialogAddVisible: false,
            dialogEditVisible: false,
            addForm: {
                name: '',
                description: '',
            },
            addRules: {

                    name: [
                        { required: true, message: '请输入名称', trigger: 'change' }
                    ],
                    description: [
                        { required: true, message: '请输入描述', trigger: 'change' }
                    ]
                },
            editForm: {
                name: '',
                description: '',
            },
            editRules: {

                    name: [
                        { required: true, message: '请输入名称', trigger: 'change' }
                    ],
                    description: [
                        { required: true, message: '请输入描述', trigger: 'change' }
                    ]
                },    
            }
    },
    methods: {
        getALLTasksFun(){  //获取所有的任务数据
            getAllTasks().then(data=>{
                let success = data.data.success
                if (success){
                    this.taskList = data.data.data;
                }else{
                    this.$notify.error({
                         title: '错误',
                         message: '请求失败'
                   });
                }
            });
        },
        openAddModel(){         //这是打开创建任务的dialog弹框
             this.dialogAddVisible = true;
        },
        openEditModel(data){    //这是打开编辑任务的dialog弹框
            this.dialogEditVisible = true;
            this.editForm.id = data.id;
            this.editForm.name = data.name;
            this.editForm.description = data.description;
        },
        addTaskFun(){   //这是请求添加任务
            this.$refs.addFormRef.validate((valid) => {
                if (valid) {
                    addTask(this.addForm).then(data=>{
                        let success = data.data.success;
                        if (success){
                            this.dialogAddVisible = false;
                            this.getALLTasksFun();
                        }else{
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
        eidtTaskFun(){    // 这是请求编辑任务
            this.$refs.editFormRef.validate((valid)=>{
                if (valid){
                    updateTask(this.editForm.id, this.editForm).then(data=>{
                        let success = data.data.success;
                        if (success){
                            this.dialogEditVisible = false;
                            this.getALLTasksFun();
                        }
                    });
                }
            });
        },
        deleteTaskFun(data){  // 这是请求删除任务
            this.$confirm(`是否确定要删除: ${data.name}`,'警告', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              dangerouslyUseHTMLString: true,
              type: 'warning'
            }).then(() => {
              deleteTask(data.id).then(data=>{
                  let success = data.data.success
                  if (success){
                     this.getALLTasksFun();
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
        resetAddForm(formName) {    // 对整个添加任务的表单进行重置，将所有字段值重置为初始值并移除校验结果
            this.$refs[formName].resetFields();
        },
        resetEditForm(formName){   // 对整个编辑任务的表单进行重置，将所有字段值重置为初始值并移除校验结果
            this.$refs[formName].resetFields();
        }
        
    },
    created() {
        this.getALLTasksFun();
    }
}
</script>

<style>
    .el-card__header {
        padding: 10px 20px;
        border-bottom: 1px solid #EBEEF5;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }

</style>

<style scoped>
    .task-main {
        text-align: left;
        padding: 10px 10px;
    }
    .task-list {
      display: flex;
      flex-wrap: wrap;
    }
    .task-card {
      width: 300px;
      margin-top: 5px;
      margin-right: 10px;  
    }
    .task-card-header {
      display: flex;
      justify-content: space-between;
  }
</style>