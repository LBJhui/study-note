<template>
	<view class="container">
		<!-- 搜索框 -->
		<view class="search-container">
			<text class="icon iconfont search-icon">&#xe747;</text>
			搜索
		</view>
		<!-- 轮播图 暂时只有一张图，先做成静态-->
		<view class="image-container">
			<image src="../../static/image/index-carousel.png" mode="widthFix"></image>
		</view>
		<!-- 内容区域 -->
		<view class="content-container">
			<view class="content-item">
				“行业-产品-公司”逐步深入，了解各行业
			</view>
			<view class="content-item">深研风口，潜力赛道看这里</view>
			<view class="content-item">贴心定制化设计，助力觅得合意金股</view>
			<view class="content-item">专家说/机构说/资金说，投资参考更给力</view>
		</view>
	</view>
</template>

<script setup lang="ts">
	import { reactive } from 'vue';
	const state = reactive({
		searchValue: ''
	})
	const iconClick = () => {
		console.log('点击搜索')
	}
</script>

<style lang="less" scoped>
	.container {
		.search-container {
			width: 688rpx;
			background: #F1F3F5;
			border-radius: 44rpx;
			font-size: 28rpx;
			color: #BAC0CC;
			line-height: 60rpx;
			margin: 32rpx auto;
			padding-left: 34rpx;

			.search-icon {
				display: inline-block;
				margin-right: 12rpx;
			}
		}

		.image-container {
			margin: 0 auto;
			width: 660rpx;

			image {
				width: 100%;
			}
		}

		.content-container {
			margin-top: 46rpx;
			padding: 0 46rpx;
			display: grid;
			grid-template-columns: 1fr 1fr;
			grid-gap: 46rpx;

			.content-item {

				background-color: #ccc;
			}
		}
	}
</style>