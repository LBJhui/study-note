<template>
  <div class="app-container">
    <div class="bg-color absolute">
      <div class="bg-yellow"></div>
      <img src="../../assets/img/bg-yellow.png" class="bg-yellow" />
      <img src="../../assets/img/bg-blue.png" class="bg-blue" />
    </div>
    <div class="main-container absolute">
      <div class="top-logo">
        <img src="../../assets/img/logo-upleft-white.png" />
      </div>
      <div class="intro-container flex-box">
        <div class="intro-item">
          <div class="circle">
            <img src="../../assets/img/circle-blue.png" />
          </div>
          <div class="intro-title">华鑫介绍</div>
        </div>
        <div class="intro-item">
          <div class="circle">
            <img src="../../assets/img/circle-blue.png" />
          </div>
          <div class="intro-title">鑫科介绍</div>
        </div>
        <div class="intro-item">
          <div class="circle">
            <img src="../../assets/img/circle-blue.png" />
          </div>
          <div class="intro-title">N视界介绍</div>
        </div>
        <div class="intro-item" @click="gotoPage('N-sight')">
          <div class="circle">
            <img src="../../assets/img/circle-blue.png" />
          </div>
          <div class="intro-title">N视界官网</div>
        </div>
      </div>

      <div class="bottom-log">N-sight ｜ πspace</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { reactive } from 'vue'
let router = useRouter()
const gotoPage = (page: string) => {
  switch (page) {
    case 'N-sight':
      router.push({ path: '/intro' })
      break
  }
}
</script>

<style scoped lang="less">
.app-container {
  width: @screenWidth;
  height: @screenHeight;
  background-color: #fff;
  position: relative;
  .flex-box {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .absolute {
    position: absolute;
    top: 0;
    left: 0;
  }
  .bg-color {
    width: 100%;
    height: 100%;
    .bg-blue {
      position: absolute;
      display: inline-block;
      bottom: 0;
      left: 0;
      width: @screenWidth;
    }
  }

  .main-container {
    width: @screenWidth;
    height: @screenHeight;

    .top-logo {
      display: inline-block;
      width: 446px;
      height: 140px;
      margin: 51px 0 0 55px;
      img {
        width: 100%;
      }
    }

    .intro-container {
      margin: 100px 0 0 56px;
      .intro-item {
        width: 408px;
        height: 606px;
        background: #ffffff;
        box-shadow: 0px 10px 30px 5px rgba(28, 50, 122, 0.15);
        border-radius: 36px;
        margin-right: 59px;

        .circle {
          width: 306px;
          height: 306px;
          margin: 100px auto 34px;
          img {
            width: 100%;
          }
        }

        .intro-title {
          text-align: center;
          font-size: 48px;
          font-weight: 600;
          color: #000000;
          line-height: 67px;
        }
      }
    }

    .bottom-log {
      position: absolute;
      width: 260px;
      height: 42px;
      font-size: 30px;
      color: #e5e7ea;
      line-height: 42px;
      bottom: 41px;
      left: 50%;
      transform: translateX(-50%);
    }
  }
}
</style>
