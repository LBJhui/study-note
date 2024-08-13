const UPLOAD_INFO = {
  NO_FILE: '请先选择文件',
  INVALID_TYPE: '不支持该类型文件上传',
  UPLOAD_FAILED: '上传失败',
  UPLOAD_SUCCESS: '上传成功',
}

const ALLOWED_TYPE = {
  'video/mp4': 'mp4',
  'video/ogg': 'ogg',
}

const CHUNK_SIZE = 1024 * 1024

const BASE_URL = 'http://localhost:8000'

const API = {
  UPLOAD_VIDEO: BASE_URL + '/upload_video',
}

;((doc) => {
  const oProgress = doc.querySelector('#uploadProgress')
  const oUpload = doc.querySelector('#videoUploader')
  const oInfo = doc.querySelector('#uploadInfo')
  const oBtn = doc.querySelector('#uploadBtn')

  let uploadedSize = 0
  let uploadedResult = null

  const init = () => {
    bindEvent()
  }

  function bindEvent() {
    oBtn.addEventListener('click', uploadVideo, false)
  }

  async function uploadVideo() {
    const file = oUpload.files[0]
    // const {
    //   files: [file],
    // } = oUpload
    if (!file) {
      oInfo.innerHTML = UPLOAD_INFO['NO_FILE']
      return
    }
    if (!ALLOWED_TYPE[file.type]) {
      oInfo.innerHTML = UPLOAD_INFO['INVALID_TYPE']
      return
    }
    // lastModified:1716356958329
    // lastModifiedDate:Wed May 22 2024 13:49:18 GMT+0800 (中国标准时间) {}
    // name:"第七节课程视频.mp4"
    // size:192707785
    // type:"video/mp4"
    // webkitRelativePath:""
    const { name, size, type } = file
    const fileName = new Date().getTime() + '_' + name
    oProgress.max = size
    oInfo.innerHTML = ''
    while (uploadedSize < size) {
      const fileChunk = file.slice(uploadedSize, uploadedSize + CHUNK_SIZE)
      const formData = createFormData({ name, type, size, fileName, uploadedSize, file: fileChunk })
      try {
        uploadedResult = await axios.post(API.UPLOAD_VIDEO, formData)
      } catch (error) {
        oInfo.innerHTML = UPLOAD_INFO['UPLOAD_FAILED'] + error.msg
      }
      uploadedSize += fileChunk.size
      oProgress.value = uploadedSize
    }
    oInfo.innerHTML = UPLOAD_INFO['UPLOAD_SUCCESS']
    oUpload.value = null
    createVideo(uploadedResult.data.video_url)
  }

  function createFormData({ name, type, size, fileName, uploadedSize, file }) {
    const fd = new FormData()
    fd.append('name', name)
    fd.append('type', type)
    fd.append('size', size)
    fd.append('fileName', fileName)
    fd.append('uploadedSize', uploadedSize)
    fd.append('file', file)
    return fd
  }

  function createVideo(src) {
    const oVideo = doc.createElement('video')
    oVideo.controls = true
    oVideo.width = 500
    oVideo.src = src
    doc.body.appendChild(oVideo)
  }
  init()
})(document)
