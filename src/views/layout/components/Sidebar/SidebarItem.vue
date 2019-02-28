<template>
  <div>
    <div class="menu-wrapper">
      <template>
        <router-link :to="'/dashboard'">
          <el-menu-item index="aq222">
            <i class="fas fa-chart-bar fa-fw"></i>
            <span slot="title">Dashboard</span>
          </el-menu-item>
        </router-link>
        <!--<router-link :to="'/addVocabulary'">-->
          <!--<el-menu-item index="Vocabulary">-->
            <!--<i class="fas fa-plus-square"></i>-->
            <!--<span slot="title">Add Vocabulary</span>-->
          <!--</el-menu-item>-->
        <!--</router-link>-->
        <router-link :to="'/topic'">
          <el-menu-item index="Study">
            <i class="fas fa-address-card"></i>
            <span slot="title">Study by topic</span>
          </el-menu-item>
        </router-link>
        <router-link :to="'/confuse'">
          <el-menu-item index="confuse">
            <i class="fas fa-mortar-pestle"></i>
            <span slot="title">Study by confuse</span>
          </el-menu-item>
        </router-link>
        <!--<router-link :to="'/dashboard'">-->
          <!--<el-menu-item index="listen">-->
            <!--<i class="fas fa-assistive-listening-systems"></i>-->
            <!--<span slot="title">Listen</span>-->
          <!--</el-menu-item>-->
        <!--</router-link>-->
        <!--<router-link :to="'/dashboard'">-->
          <!--<el-menu-item index="Read">-->
            <!--<i class="fab fa-readme"></i>-->
            <!--<span slot="title">Read</span>-->
          <!--</el-menu-item>-->
        <!--</router-link>-->
        <!--===========================================================-->
        <!--<el-submenu popper-class="vcc-pbx-menu" index="1" class="aaa">-->
          <!--<template slot="title">-->
            <!--<i class="fas fa-user-cog fa-fw"></i>-->
            <!--<span>Customers</span>-->
          <!--</template>-->
          <!--<el-menu  background-color="#2a3a49" text-color="#fff">-->
            <!--<div style="background-color: #0e1f31c2!important;padding: 20px;padding-bottom: 0px;padding-top: 10px">-->
              <!--<el-input size="small" type="text" placement="searchft" prefix-icon="el-icon-search" placeholder="Search account ..." v-model="searchkey" clearable></el-input>-->
            <!--</div>-->
            <!--<div style="background-color: #0e1f31c2!important;padding: 20px;padding-bottom: 0px;padding-top: 10px;padding-bottom: 10px">-->
              <!--<el-select size="small" @click="filtered" v-model="filters" placeholder="Select">-->
                <!--<el-option @click.native="filtered" label="All" value=""></el-option>-->
                <!--<el-option @click.native="filtered" label="Active" value="active"></el-option>-->
                <!--<el-option @click.native="filtered" label="Pending" value="pending"></el-option>-->
                <!--<el-option @click.native="filtered" label="Progress" value="progress"></el-option>-->
              <!--</el-select>-->
            <!--</div>-->
            <!--<el-submenu @click="PushAccount(acc.id)"  :index="acc.email" v-for="acc in accounts" :key="acc.email">-->
              <!--<template @click="PushAccount(acc.id)" slot="title" text-color="#ffffff">-->
                <!--<router-link :to="'/account/' + acc.id" >-->
                  <!--&lt;!&ndash;<i class="fas fa-chart-bar fa-fw"></i>&ndash;&gt;-->
                  <!--<div>-->
                    <!--<span  style="word-wrap: break-word;font-size: 13px">{{acc.email}}</span>-->
                    <!--<el-tag size="mini" v-if="acc.status==='prog'" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else-if="acc.status==='active'" type="success" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else type="warning" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-if="acc.status==='prog'" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else-if="acc.status==='active'" type="success" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else type="warning" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-if="acc.status==='prog'" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else-if="acc.status==='active'" type="success" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                    <!--<el-tag size="mini" v-else type="warning" class="sidebar-item-button">{{acc.status}} {{acc.hotlines.length}}</el-tag>-->
                  <!--</div>-->
                <!--</router-link>-->
                <!--&lt;!&ndash;</el-badge>&ndash;&gt;-->
              <!--</template>-->
              <!--<router-link :to="'/addhotline/' + acc.id">-->
               <!--<el-menu-item index="aq2" style="margin-right: 10px">-->
                 <!--<i style="color: #3798ec" class="fas fa-plus"></i>-->
                 <!--<el-button style="font-size: 17px;padding-left: 12px" type="text">Thêm hotline</el-button>-->
               <!--</el-menu-item>-->
              <!--</router-link>-->
              <!--<el-menu-item v-if="acc.hotlines.length > 0" index="aq" class="center-number">-->
                <!--&lt;!&ndash;number of accounts&ndash;&gt;-->
                  <!--<el-input size="small" prefix-icon="el-icon-search" clearable placeholder="Search ..." v-model="searht"></el-input>-->
              <!--</el-menu-item>-->
              <!--<el-menu-item @click="phonerouter(hotl.id)" v-if="searht!==''&& check_search(searht,hotl.number)" :index="hotl.number" v-for="hotl in acc.hotlines" :key="hotl.number">-->
                <!--<router-link :to="'/hotline_account/' + hotl.id">-->
                  <!--<i class="fas fa-phone-square fa-fw"></i>-->
                  <!--<span>{{formatPhone(hotl.number)}}</span>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                <!--</router-link>-->
              <!--</el-menu-item>-->
              <!--<el-menu-item  @click="phonerouter(hotl.id)" v-if="searht===''&& check_search('0',hotl.number)" :index="hotl.number" v-for="hotl in acc.hotlines" :key="hotl.number">-->
                <!--<router-link :to="'/hotline_account/' + hotl.id">-->
                  <!--<i class="fas fa-phone-square fa-fw"></i>-->
                  <!--<span>{{formatPhone(hotl.number)}}</span>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-if="hotl.status==='progress'" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='pending'" type="warning" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else-if="hotl.status==='active'" type="success" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                  <!--<el-tag v-else type="danger" class="sidebar-item-button">{{hotl.status}}</el-tag>-->
                <!--</router-link>-->
              <!--</el-menu-item>-->
            <!--</el-submenu>-->
          <!--</el-menu>-->
          <!--&lt;!&ndash;<b-pagination align="center" size="md" :total-rows="k" v-model="pag" :per-page="10"></b-pagination>&ndash;&gt;-->
        <!--</el-submenu>-->
        <!--<el-submenu popper-class="vcc-pbx-menu" index="hotw">-->
          <!--<template slot="title">-->
            <!--<i class="fas fa-phone-square fa-fw"></i>-->
            <!--<span>Hotlines</span>-->
          <!--</template>-->
          <!--&lt;!&ndash;<el-menu  background-color="#1a2835" text-color="#fff">&ndash;&gt;-->
            <!--&lt;!&ndash;<div style="padding: 20px;padding-bottom: 0px;padding-top: 10px">&ndash;&gt;-->
              <!--&lt;!&ndash;<router-link :to="'/addHotline'">&ndash;&gt;-->
                <!--&lt;!&ndash;<i style="color: #3798ec" class="fas fa-plus"></i>&ndash;&gt;-->
                <!--&lt;!&ndash;<el-button style="font-size: 17px;padding-left: 12px" type="text">Thêm hotline vào kho</el-button>&ndash;&gt;-->
                <!--&lt;!&ndash;&lt;!&ndash;<el-button type="text" @click="dialogVisible = true">click to open the Dialog</el-button>&ndash;&gt;&ndash;&gt;-->
              <!--&lt;!&ndash;</router-link>&ndash;&gt;-->

<!--&lt;!&ndash;&lt;!&ndash;==================================================================================================================&ndash;&gt;&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
            <!--&lt;!&ndash;<div style="background-color: #0e1f31c2!important;padding: 20px;padding-bottom: 0px;padding-top: 10px">&ndash;&gt;-->
              <!--&lt;!&ndash;<el-input size="small" @keyup.enter.native="gethotlines(pag)" placeholder="Search number ..." v-model="searchkeys" prefix-icon="el-icon-search" clearable></el-input>&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
            <!--&lt;!&ndash;<div style="background-color: #0e1f31c2!important;padding: 20px;padding-bottom: 0px;padding-top: 10px;padding-bottom: 10px">&ndash;&gt;-->
              <!--&lt;!&ndash;<el-select size="small" @click="filteredht(pag)" v-model="filterss" placeholder="Select">&ndash;&gt;-->
                <!--&lt;!&ndash;<el-option @click.native="filteredht(pag)" label="All" value=""></el-option>&ndash;&gt;-->
                <!--&lt;!&ndash;<el-option @click.native="filteredht(pag)" label="Normal" value="Normal"></el-option>&ndash;&gt;-->
                <!--&lt;!&ndash;<el-option @click.native="filteredht(pag)" label="VIP" value="VIP"></el-option>&ndash;&gt;-->
              <!--&lt;!&ndash;</el-select>&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
            <!--&lt;!&ndash;<el-menu-item @click="teee(num.number)" :index="num.number" class="center-number" v-for="num in hotlines" :key="num.number">&ndash;&gt;-->
              <!--&lt;!&ndash;<router-link :to="'/hotline/'+num.number">&ndash;&gt;-->
                <!--&lt;!&ndash;<div>&ndash;&gt;-->
                  <!--&lt;!&ndash;<i class="fas fa-phone-square fa-fw"></i>&ndash;&gt;-->
                  <!--&lt;!&ndash;<span>{{formatPhone(num.number)}}</span>&ndash;&gt;-->
                  <!--&lt;!&ndash;<el-tag v-if="num.kind==='Normal'" class="sidebar-item-button" type="success">{{num.status}} {{num.kind}}</el-tag>&ndash;&gt;-->
                  <!--&lt;!&ndash;<el-tag v-else class="sidebar-item-button" type="danger">{{num.status}} {{num.kind}}</el-tag>&ndash;&gt;-->
                  <!--&lt;!&ndash;<el-tag v-if="num.kind==='Normal'" class="sidebar-item-button" type="success">{{num.status}} {{num.kind}}</el-tag>&ndash;&gt;-->
                  <!--&lt;!&ndash;<el-tag v-else class="sidebar-item-button" type="danger">{{num.status}} {{num.kind}}</el-tag>&ndash;&gt;-->
                  <!--&lt;!&ndash;<el-tag v-if="num.kind==='Normal'" class="sidebar-item-button" type="success">{{num.status}} {{num.kind}}</el-tag>&ndash;&gt;-->
                <!--&lt;!&ndash;</div>&ndash;&gt;-->
              <!--&lt;!&ndash;</router-link>&ndash;&gt;-->
            <!--&lt;!&ndash;</el-menu-item>&ndash;&gt;-->
          <!--&lt;!&ndash;</el-menu>&ndash;&gt;-->
          <!--<div style="padding-left: 60px;background-color: #17212e;padding-bottom: 7px">-->
            <!--<el-pagination-->
              <!--small-->
              <!--style="color: #4b494e"-->
              <!--:current-page.sync="pag"-->
              <!--:page-size="12"-->
              <!--layout="prev, pager, next"-->
              <!--:total="k">-->
            <!--</el-pagination>-->
          <!--</div>-->
          <!--&lt;!&ndash;</el-menu-item>&ndash;&gt;-->
        <!--</el-submenu>-->
        <!--<router-link :to="'/packages'">-->
          <!--<el-menu-item index="pac">-->
            <!--<i class="fas fa-box"></i>-->
            <!--<span slot="title">Packages</span>-->
          <!--</el-menu-item>-->
        <!--</router-link>-->
        <!--<router-link :to="'/addons'">-->
          <!--<el-menu-item index="addon">-->
            <!--<i class="fas fa-puzzle-piece"></i>-->
            <!--<span slot="title">Addons</span>-->
          <!--</el-menu-item>-->
        <!--</router-link>-->
        <!--</el-submenu>-->
        <router-link :to="'/history'">
          <el-menu-item index="history">
            <i class="fas fa-history"></i>
            <span slot="title">Study</span>
          </el-menu-item>
        </router-link>
      </template>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import VueSingleSelect from 'vue-single-select'
export default {
  name: 'SidebarItem',
  components: {
    VueSingleSelect
  },
  data() {
    return {
      numberOffice: '',
      numberService: '',
      temp: [],
      tempOffice: [],
      tempService: [],
      accounts: '',
      searchkey: '',
      searchkeys: '',
      filters: '',
      filterss: '',
      hotlines: '',
      k: 1,
      pag: 1,
      searht: '',
      searchbill: ''
      // ============
    }
  },
  watch: {
    'pag'() {
      // console.log(this.pag)
      this.gethotlines(this.pag)
    },
    'filters'() {
      this.pag = 1
    },
    'searchkeys'() {
      if (this.searchkeys === '') {
        this.gethotlines(this.pag)
      }
    },
    '$store.state.hide.update'() {
      // console.log('vudeptrai=========')
      if (this.$session.get('otp')) {
        this.getall()
      }
    },
    'searchbill'() {
      this.getall(this.searchbill)
    },
    'searchkey'() {
      this.getall(this.searchkey)
    }
    // '$store.state.check_add_hotline'() {
    //   this.gethotlines(this.pag)
    //   this.$store.state.check_add_hotline = ''
    // },
    // 'searchkey'() {
    //   if (this.searchkey === '') {
    //     this.gethotlines(this.pag)
    //   }
    // }
  },
  mounted() {
    // this.getall()
    // this.gethotlines(this.pag)
    // console.log('aaaaaaaaaa' + this.routes[0].toString())
  },
  computed: {
    ...mapGetters(['sidebar'])
  },
  methods: {
    getall(key) {
      // this.$http.get(process.env.SWAPI_URL + '/account', { headers: { 'Authorization': this.$session.get('token') }, params: { status: this.filters, keyword: key }})
      //   .then(function(response) {
      //     // console.log(response)
      //     // console.log(response)
      //     if (response.body.status === true) {
      //       this.accounts = response.data.data
      //       // console.log(response.data.data)
      //     }
      //   }, respone => {
      //     if (respone.body.status === false) {
      //       // this.$session.destroy()
      //       // this.$cookies.remove('token')
      //       // this.$cookies.remove('otp')
      //       // this.$router.push('/login')
      //     }
      //   })
    },
    gethotlines(page) {
      // this.$http.get(process.env.SWAPI_URL + '/hotline', { headers: { 'Authorization': this.$session.get('token') }, params: { store: 'yes', offset: page, limit: 12, status: this.filterss, keyword: this.searchkeys }})
      //   .then(function(response) {
      //     if (response.body.status === true) {
      //       this.hotlines = response.data.data
      //       this.k = response.data.total
      //       console.log('this is k' + this.k)
      //     }
      //   }, respone => {
      //     if (respone.body.status === false) {
      //       this.$session.destroy()
      //       this.$cookies.remove('token')
      //       this.$cookies.remove('otp')
      //       this.$router.push('/login')
      //     }
      //   })
    },
    check_search(key, list) {
      return list.includes(key)
    },
    a() {
      alert('aaaa')
    },
    filtered() {
      // this.$http.get(process.env.SWAPI_URL + '/account', { headers: { 'Authorization': this.$session.get('token') }, params: { status: this.filters }})
      //   .then(function(response) {
      //     this.accounts = response.data.data
      //   })
    },
    filteredht(page) {
      // this.$http.get(process.env.SWAPI_URL + '/hotline', { headers: { 'Authorization': this.$session.get('token') }, params: { store: 'yes', offset: page, limit: 12, kind: this.filterss }})
      //   .then(function(response) {
      //     // console.log(this.filters)
      //     this.hotlines = response.data.data
      //     this.hotlines = response.data.data
      //     this.k = response.data.total
      //     console.log('aaaaaeeeeeeeeeeeeeeee' + this.k)
      //   })
    },
    formatPhone(obj) {
      var numbers = obj.replace(/\D/g, '')
      var char = { 4: '.', 7: '.' }
      obj = ''
      for (var i = 0; i < numbers.length; i++) {
        obj += (char[i] || '') + numbers[i]
      }
      return obj
    },
    hasOneShowingChildren(children) {
      const showingChildren = children.filter(item => {
        return !item.hidden
      })
      if (showingChildren.length === 1) {
        return true
      }
      return false
    },
    handleClickToggle() {
      if (!this.sidebar.opened) this.$store.dispatch('toggleSideBar')
    },
    search(keyword, item) {
      return item.includes(keyword)
    },
    teee(id) {
      this.$router.push('/hotline/' + id)
    },
    click(email) {
      this.$router.push('/billing/' + email)
    },
    // teeeee(id) {
    //   this.$router.push('/billing/' + id)
    // },
    PushAccount(id) {
      alert(id)
      // console.log('aaaaaaaaaa')
      // this.$router.push('/account/' + id)
    },
    phonerouter(id) {
      this.$router.push('/hotline_account/' + id)
    }
  }
}
</script>

<style>
  .submenu-has-icon .el-submenu__title,
  .submenu-has-icon .el-menu-item {
    padding-left: 20px!important;
  }

  #app .el-submenu .submenu-has-no-icon.el-menu-item {
    padding-left: 40px!important;
    background-color: #0e1f31c2!important;
  }

  .sidebar-item-button {
    position: absolute!important;
    right: 35px;
    top: 10px;
  }

  .el-menu--vertical {
    width: 290px;
  }

  .number-index {
    font-size: 16px;
    font-weight: bold;
    margin: 0 18px 0 18px;
    padding: 18px 0 18px 0;
  }

  /*.list-numbers {*/
    /*height: 200px;*/
    /*overflow-x: hidden;*/
    /*overflow-y: scroll;*/
  /*}*/

  .nav-item-ellipsis {
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    display: block;
    max-width: 125px;
  }

  .list-numbers {
    max-height: 220px;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .list-numbers::-webkit-scrollbar {
    width: 3px;
  }

  .list-numbers::-webkit-scrollbar-thumb:vertical {
    margin: 15px;
    background-color: rgba(153, 153, 153, 0.5);
    -webkit-border-radius: 3px;
  }

  .list-numbers::-webkit-scrollbar-button:start:decrement,
  .list-numbers::-webkit-scrollbar-button:end:increment {
    height: 4px;
    display: block;
  }

  .list-numbers::-webkit-scrollbar {
    width: 4px;
  }
  .list-numbers::-webkit-scrollbar-track {
    border-radius: 3px;
    background: #060a36;
    border: 3px solid transparent;
  }
  .list-numbers::-webkit-scrollbar-thumb{
    border-radius: 3px;
    background: #18304e;
    border: 3px solid transparent;
  }

  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar {
    width: 3px;
  }

  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar-thumb:vertical {
    margin: 15px;
    background-color: rgba(153, 153, 153, 0.5);
    -webkit-border-radius: 3px;
  }

  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar-button:start:decrement,
  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar-button:end:increment {
    height: 4px;
    display: block;
  }

  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar {
    width: 4px;
  }
  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar-track {
    border-radius: 3px;
    background: #458ee9;
    border: 3px solid transparent;
  }
  body > .el-menu--vertical.vcc-pbx-menu::-webkit-scrollbar-thumb{
    border-radius: 3px;
    background: #3220df;
    border: 3px solid transparent;
  }
  .el-submenu .el-menu-item {
    height: 40px;
    line-height: 40px;
  }
  .el-menu-item, .el-submenu__title {
    height: 45px;
    line-height: 45px;
  }
  .el-menu-item.is-disabled {
    opacity: 0.5;
  }
  .el-menu--collapse .el-menu .el-submenu, .el-menu--popup {
    /*height: 560px;*/
    min-width: 387px;
    /*min-height: auto;*/
  }
  .in {
    width: 100%;
    height: 30px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box
  }
  /*------------*/
  .form-control {
    display: block;
    width: 100%;
    height: 34px;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #6e6e6e;
    background-color: #fff;
    background-image: none;
    border: 1px solid #ccc;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
    -webkit-transition: border-color ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
    -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  }
  .form-control:focus {
    border-color: #66afe9;
    outline: 0;
    -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, .6);
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, .6);
  }
  .form-control::-moz-placeholder {
    color: #999;
    opacity: 1;
  }
  .form-control:-ms-input-placeholder {
    color: #999;
  }
  .form-control::-webkit-input-placeholder {
    color: #999;
  }
  .form-control::-ms-expand {
    background-color: transparent;
    border: 0;
  }
  .form-control[disabled],
  .form-control[readonly],
  fieldset[disabled] .form-control {
    background-color: #eee;
    opacity: 1;
  }
  .form-control[disabled],
  fieldset[disabled] .form-control {
    cursor: not-allowed;
  }

</style>
