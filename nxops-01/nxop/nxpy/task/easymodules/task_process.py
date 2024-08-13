# _*_ coding: utf-8 _*_
# @Time: 2024/4/19 11:10
# @Author: LBJ辉
# @File: task_process
# @Project: nxops-01
realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "init_task_stages": ("""INSERT IGNORE INTO task.t_TaskStage(TaskID, RunID, StageID, StageTag, StageName, UpdateDate, UpdateTime, Status, Remark)
                                VALUES(#{taskID}, #{runID}, #{stageID}, #{stageTag}, #{stageName}, DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%H:%i:%S'), #{stageStatus}, #{stageRemark})""",
                         {"many": True}),
}
