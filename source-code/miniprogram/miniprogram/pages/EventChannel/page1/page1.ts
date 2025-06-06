// pages/EventChannel/page1/page1.ts
Page({
  /**
   * 页面的初始数据
   */
  data: {},
  goToPage2() {
    console.log(1);
    wx.navigateTo({
      url: "/pages/EventChannel/page2/page2",
      events: {
        // 监听目标页面发送的消息
        someEvent(data: any) {
          console.log(data); // 可以在这里处理目标页面返回的数据
        },
      },
      success: (res) => {
        // 创建要传递的复杂数据
        const arrayData = [1, 2, 3, 4, 5];
        const objectData = {
          key: "value",
          info: { nestedKey: "nestedValue" },
        };

        // 通过 EventChannel 向目标页面传递数据
        res.eventChannel.emit("someEvent", {
          array: arrayData,
          object: objectData,
        });
      },
    });
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {},

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


