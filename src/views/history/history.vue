<template>
  <div style="padding: 2%">
    <el-card shadow="never">
      <div slot="header" class="clearfix" style="position: relative;">
        <span style="font-weight: bold; font-size: 20px">Activity</span>
      </div>
      <el-table
        :data="activety"
        stripe
        style="width: 100%">
        <el-table-column
          prop="timestamp"
          label="Date_time"
          width="180">
        </el-table-column>
        <el-table-column
          prop="user"
          label="User"
          width="180">
        </el-table-column>
        <el-table-column
          prop="method"
          label="Method">
          <template slot-scope="scope">
            <div v-if="scope.row.method === 'DELETE'">
              <el-tag size="mini" type="danger">{{scope.row.method}}</el-tag>
            </div>
            <div v-else-if="scope.row.method === 'POST'">
              <el-tag size="mini" type="success">{{scope.row.method}}</el-tag>
            </div>
            <div v-else>
              <el-tag size="mini" type="warning">{{scope.row.method}}</el-tag>
            </div>
            <!--<i class="el-icon-error"></i>-->
          </template>
        </el-table-column>
        <el-table-column
          prop="endpoint"
          label="Endpoint">
        </el-table-column>
        <el-table-column
          prop="description"
          label="Description">
        </el-table-column>
      </el-table>
      <div class="block" style="margin-top: 10px; text-align: right;">
        <el-pagination
          small
          @current-change="handleCurrentChange"
          style="color: #4b494e"
          :current-page.sync="pag"
          :page-size="15"
          layout="total,prev, pager, next"
          :total="total">
        </el-pagination>
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    name: 'history',
    data() {
      return {
        show: false,
        activety: null,
        pag: 1,
        new_data: null,
        total: 0
      }
    },
    mounted() {
      this.get_method(this.pag)
    },
    methods: {
      get_method(page) {
        this.$http.get(process.env.SWAPI_URL + '/activity', { headers: { 'Authorization': this.$session.get('token') }, params: { offset: page, limit: 15 }})
          .then(function(response) {
            if (response.body.status === true) {
              this.activety = response.data.data
              this.total = response.data.total
              this.k = (parseInt(response.data.total / 15) * 10) + 1
              console.log(this.total)
            }
          }, respone => {
            if (respone.body.status === false) {
              // console.log('aaa')
              // this.$session.destroy()
              // this.$cookies.remove('token')
              // this.$cookies.remove('otp')
              // this.$router.push('/login')
            }
          })
      },
      handleCurrentChange() {
        this.get_method(this.pag)
      }
    }
  }
</script>

<style scoped>

</style>
