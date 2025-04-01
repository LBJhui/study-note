// pages/EventChannel/page2/page2.ts
Page({
  /**
   * 页面的初始数据
   */
  data: {
    receivedArray: [],
    receivedObject: {},
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {
    // 目标页面
    const eventChannel = this.getOpenerEventChannel();
    eventChannel.on("someEvent", (data) => {
      // 接收数组和对象数据
      console.log(data.array); // [1, 2, 3, 4, 5]
      console.log(data.object); // { key: 'value', info: { nestedKey: 'nestedValue' } }

      // 进行相应的数据处理
      // 例如，渲染数据到页面上
      this.setData({
        receivedArray: data.array,
        receivedObject: data.object,
      });
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {},

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {},

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {},

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {},

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {},

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {},

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {},
});
