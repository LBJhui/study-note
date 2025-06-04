// 自动文件备份
const fs = require('fs')
const path = require('path')

function backupFiles(sourceFolder, backupFolder) {
  fs.readdir(sourceFolder, (err, files) => {
    if (err) throw err
    files.forEach((file) => {
      const sourcePath = path.join(sourceFolder, file)
      const backupPath = path.join(backupFolder, file)
      fs.copyFile(sourcePath, backupPath, (err) => {
        if (err) throw err
        console.log(`Backed up ${file}`)
      })
    })
  })
}

const source = './path'
const backup = './backup'
backupFiles(source, backup)
