<template>
  <div>
    <el-dialog title="Thông tin addon cần thêm" :visible.sync="dialogFormVisible" width="45%">
      <el-form>
        <el-form-item>
          <el-row>
            <el-col :span="12" style="padding-left: 40px"><strong>Tên addon</strong></el-col>
            <el-col :span="12" style="padding-right: 40px"><el-input v-model="further_name" placeholder="Tên package"></el-input></el-col>
          </el-row>
          <el-row style="padding-top: 20px">
            <el-col :span="12" style="padding-left: 40px"><strong>Giá</strong></el-col>
            <el-col :span="12" style="padding-right: 40px"><el-input-number :min="1" :max="1000000000" v-model="further_price" size="medium"></el-input-number></el-col>
          </el-row>
          <el-row style="padding-top: 20px">
            <el-col :span="12" style="padding-left: 40px"><strong>Tính năng</strong>
              <el-button @click="add_further_feature" size="mini" style="padding-left: 10px" type="primary"><i class="fas fa-plus-circle"></i> Thêm tính năng</el-button>
            </el-col>
          </el-row>
          <el-row style="padding-left: 40px">
            <el-table
              :data="further_feature"
              style="width: 100%">
              <el-table-column
                label="Valuess">
                <template slot-scope="scope">
                  <div>
                    <el-input placeholder="Tính năng" v-model="scope.row.value" clearable></el-input>
                  </div>
                </template>
              </el-table-column>
              <el-table-column
                align="right"
                width="40"
              >
                <template slot-scope="scope">
                  <!--<i class="el-icon-error"></i>-->
                  <el-button @click="pop_item(scope.$index)" circle size="mini" type="danger" plain icon="el-icon-error"></el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-row>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="add_addon">Confirm</el-button>
    <!--<el-button type="primary" @click="dialogFormVisible = false">Confirm</el-button>-->
  </span>
    </el-dialog>
    <el-row style="padding-top: 8px">
      <el-col :span="14">
        <div class="app-container" style="padding-left: 20px">
          <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :md="24">
              <el-card shadow="never">
                <div slot="header" class="clearfix" style="position: relative;">
                  <span style="font-weight: bold; font-size: 20px">Addon normal</span>
                  <el-button @click="dialogFormVisible = true" size="mini" style="padding-left: 10px" type="primary"><i class="fas fa-plus-circle"></i> Thêm mới</el-button>
                </div>
                <el-row :gutter="20" style="margin-left: 0!important; margin-right: 0!important; margin-top: 30px">
                  <el-col :span="8" v-for="ad in addons_ql" :key="ad.id">
                    <center>
                      <el-card class="box-style" @click.native="selectPack(ad)" :class="{'style-select': ad.check}">
                        <div slot="header">
                          {{ad.name}}
                        </div>
                        <div>
                          <p class="price-cover"><span class="price">{{ad.price | formatMoney}}</span></p>
                          <p style="padding-top: 20px">Value {{ad.value}}</p>
                          <p style="padding-top: 20px">Unit {{ad.unit}}</p>
                        </div>
                      </el-card>
                    </center>
                  </el-col>
                </el-row>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-col>
      <el-col :span="10">
        <div class="app-container" style="padding-right: 10px;padding-left: 0px">
          <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :md="24">
              <el-card shadow="never">
                <div slot="header" class="clearfix" style="position: relative;">
                  <span style="font-weight: bold; font-size: 20px">Thông tin Addon</span>
                  <div style="float: right">
                    <el-button icon="el-icon-delete" type="danger" @click="open2" plain>Xoá</el-button>
                  </div>
                </div>
                <el-row>
                  <el-col :span="12">
                    <strong>Tên gói :</strong>
                  </el-col>
                  <el-col :span="12">
                    <center v-show="!edit">{{name}}</center>
                    <el-input v-show="edit" placeholder="Tên gói" v-model="name" clearable></el-input>
                  </el-col>
                </el-row>
                <el-row style="padding-top: 40px">
                  <el-col :span="12">
                    <strong>Chi phí :</strong>
                  </el-col>
                  <el-col :span="12">
                    <center v-show="!edit" style="color: red">{{price | formatMoney}} VNĐ</center>
                    <el-input-number style="width: 100%" :min="1" :max="1000000000" v-show="edit" v-model="price" :step="5"></el-input-number>
                  </el-col>
                </el-row>
                <el-row style="padding-top: 40px">
                    <strong>Tính năng</strong>
                    <el-button v-show="edit" @click="add_feature" size="mini" style="padding-left: 10px" type="primary"><i class="fas fa-plus-circle"></i> Thêm</el-button>
                </el-row>
                <el-row>
                  <el-col>
                    <el-table
                      :data="feature"
                      style="width: 100%">
                      <el-table-column
                        label="Value">
                        <template slot-scope="scope">
                          <div v-show="!edit">
                            {{scope.row.value}}
                            <!--<el-input placeholder="Tính năng" v-model="scope.row.value" clearable></el-input>-->
                          </div>
                          <div v-show="edit">
                            <el-input placeholder="Tính năng" v-model="scope.row.value" clearable></el-input>
                          </div>
                        </template>
                      </el-table-column>
                      <el-table-column
                        align="right"
                        width="40"
                      >
                        <template slot-scope="scope">
                          <!--<i class="el-icon-error"></i>-->
                          <el-button :disabled="!edit" @click="pop_item_edit(scope.$index)" circle size="mini" type="danger" plain icon="el-icon-error"></el-button>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                </el-row>
                <el-row style="padding-left: 80px;padding-top: 30px">
                  <!--<el-checkbox v-model="checkedRules" style="display: inline-block !important;"></el-checkbox> Đọc và xác nhận các <a @click="showRule" style="color: #1e6abc">điều khoản</a> của chúng tôi.-->
                </el-row>
                <el-row style="padding-top: 35px" v-show="!edit">
                  <center><el-button @click="edit = true" type="primary" icon="el-icon-edit">Sửa đổi</el-button></center>
                </el-row>
                <el-row style="padding-top: 15px" v-show="edit">
                  <center>
                    <el-button @click="open3" type="success" plain>Lưu</el-button>
                    <el-button @click="cancle" plain>Huỷ</el-button>
                  </center>
                </el-row>
                <!--<el-row style="padding-top: 40px">-->
                <!--<el-checkbox v-model="checked" style="display: inline-block !important;">Đọc và đồng ý các </el-checkbox><a @click="open"> điều khoản</a> của chúng tôi-->
                <!--<span style="padding-left: 80px">điều khoản</span>-->
                <!--</el-row>-->
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'add_normal',
    data() {
      return {
        addons_ql: [],
        // =====
        name: '',
        value: 1,
        price: 10000,
        unit: '',
        edit: false,
        id: '',
        dialogFormVisible: false,
        feature: [],
        // =====
        further_name: '',
        further_value: 0,
        further_unit: 'MB',
        further_price: 1,
        further_feature: [{ value: 'minhvu' }, { value: 'deptrai' }, { value: 'hocgioi' }]
      }
    },
    mounted() {
      this.get_addon_user()
    },
    methods: {
      get_addon_user() {
        this.$http.get(process.env.SWAPI_URL + '/addon', { headers: { 'Authorization': this.$session.get('token') }})
          .then(function(response) {
            const arr = []
            if (response.body.status === true) {
              for (let i = 0; i < response.data.data.length; i++) {
                if (response.data.data[i].kind === 'normal') {
                  arr.push(response.data.data[i])
                }
              }
              for (const i in arr) {
                arr[i]['check'] = false
              }
              this.addons_ql = arr
              this.addons_ql[0].check = true
              this.name = this.addons_ql[0].name
              this.value = this.addons_ql[0].value
              this.price = this.addons_ql[0].price
              this.unit = this.addons_ql[0].unit
              this.id = this.addons_ql[0].id
              var fea = this.addons_ql[0].feature
              var k = []
              for (const i in fea) {
                var m = { value: fea[i] }
                k.push(m)
              }
              this.feature = k
            }
            console.log(this.addons_ql)
          })
      },
      selectPack(add) {
        this.name = add.name
        this.value = add.value
        this.price = add.price
        this.unit = add.unit
        this.id = add.id
        var k = []
        for (const i in add.feature) {
          var m = { value: add.feature[i] }
          k.push(m)
        }
        this.feature = k
        // this.feature = add.feature
        if (add.check === false) {
          add.check = true
          for (const i in this.addons_ql) {
            if (this.addons_ql[i].id !== add.id) {
              this.addons_ql[i].check = false
            }
          }
        }
      },
      cancle() {
        this.edit = false
        this.get_addon_user()
      },
      add_addon() {
        var k = []
        for (const i in this.further_feature) {
          k.push(this.further_feature[i].value)
        }
        if (this.further_name === '') {
          this.$message.error('Tên addon trống !')
        } else {
          const newIp = {
            name: this.further_name,
            price: this.further_price,
            kind: 'normal',
            feature: k
          }
          this.$http.post(process.env.SWAPI_URL + '/addon', newIp, { headers: { 'Authorization': this.$session.get('token') }})
            .then(function(response) {
              if (response.body.status === true) {
                this.$notify({
                  title: 'Success',
                  message: response.body.message,
                  type: 'success'
                })
                this.get_addon_user()
              }
            }, respone => {
              this.$notify.error({
                title: 'Error',
                message: respone.body.message
              })
            })
        }
      },
      delete_addon() {
        const newIp = {
          id: this.id
        }
        this.$http.delete(process.env.SWAPI_URL + '/addon', { headers: { 'Authorization': this.$session.get('token') }, body: newIp })
          .then(function(response) {
            if (response.body.status === true) {
              this.$notify({
                title: 'Success',
                message: response.body.message,
                type: 'success'
              })
              this.get_addon_user()
            }
          }, respone => {
            this.$notify.error({
              title: 'Error',
              message: respone.body.message
            })
          })
      },
      open2() { // xóa package
        this.$confirm('Xoá addon ' + this.name + ' . Tiếp tục?', 'Xác nhận', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          this.delete_addon()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete canceled'
          })
        })
      },
      edit_addon: function() {
        var data = []
        for (const i in this.feature) {
          data.push(this.feature[i].value)
        }
        if (this.name === '') {
          this.$message.error('Tên addon trống !')
        } else {
          const newIp = {
            id: this.id,
            name: this.name,
            price: this.price,
            kind: 'normal',
            feature: data
          }
          this.$http.put(process.env.SWAPI_URL + '/addon', newIp, { headers: { 'Authorization': this.$session.get('token') }})
            .then(function(response) {
              if (response.body.status === true) {
                this.$notify({
                  title: 'Success',
                  message: response.body.message,
                  type: 'success'
                })
                this.edit = false
                this.get_addon_user()
              }
            }, respone => {
              this.$notify.error({
                title: 'Error',
                message: respone.body.message
              })
            })
        }
      },
      open3() {
        var checks = 0
        for (const i in this.feature) {
          if (this.feature[i].value === '') {
            checks = 1
            break
          }
        }
        if (this.name === '') {
          this.$message.error('Tên addon trống !')
        } else if (checks === 1) {
          this.$message.error('Thiếu thông tin tính năng !')
        } else {
          var t = ''
          for (const i in this.addons_ql) {
            if (this.addons_ql[i].id === this.id) {
              t = this.addons_ql[i].name
            }
          }
          this.$confirm('Thay đổi thông tin addon ' + t + ' . Tiếp tục?', 'Xác nhận', {
            confirmButtonText: 'OK',
            cancelButtonText: 'Cancel',
            type: 'warning'
          }).then(() => {
            this.edit_addon()
          }).catch(() => {
            this.$message({
              type: 'info',
              message: 'Edit canceled'
            })
          })
        }
      },
      pop_item(feature) {
        this.further_feature.splice(feature, 1)
      },
      add_further_feature() {
        const new_feature = { value: '' }
        this.further_feature.unshift(new_feature)
      },
      pop_item_edit(feature) {
        this.feature.splice(feature, 1)
      },
      add_feature() {
        const new_feature = { value: '' }
        this.feature.unshift(new_feature)
      }
    }
  }
</script>

<style lang="scss">
  .title-style {
    font-size: 1em;
    font-weight: 700;
    color: #676767;
  }
  .add-hotline-form {
    .el-card__header {
      padding: 10px 20px !important;
      text-align: center !important;
      font-size: 16px;
      color: #000;
    }
    .el-card__body {
      text-align: center;
      font-size: 12px;
      .price-cover {
        margin-top: 0;
        color: #3A71A8;
        .price {
          font-size: 24px;
        }
      }
    }
  }
  .box-style{
    text-align: center;
    cursor: pointer;
    border: 1px solid #f1f1f1;
    color: #6e6e71;
    padding: 1.20rem;
  }
  .style-select {
    background: rgba(0, 136, 204, 0.05);
    border: 1px solid #0088cc;
    color: #676767;
    .el-card__body {
      .price-cover {
        color: #0088cc;
      }
    }
  }
  .hotline-info .el-card__body {
    padding-top: 0;
    padding-bottom: 0
  }
  .item{
    /*margin-top: 1.5em;*/
    padding: 1.2em 0 1em 0;
    border-bottom: 1px solid #f4f4f5;
  }
  .text {
    font-weight: bold;
    padding-left: 80px;
    font-size: 18px;
  }
</style>
