def mo6():
  commands = [
    ['drive_mm',[0, 200, 100]],
    ['wait',[200]],
    ['pivot',[35, 100]],
    ['gyro_drive',[0, 200, 630, 'True']],
    ['wait',[200]],
    ['pivot',[55, 100]],
    ['gyro_drive',[0, 200, 400, 'True']],
    ['pivot',[-60, 100]],
    ['drive_mm',[0, 150, 200]],
    ['pivot',[45, 100]],
    ['act_run_time',[-700, 1000, 'left', 'False']],
    ['act_run_time',[700, 400, 'right', 'True']],
    ['drive_mm',[0, 75, 30]],
    ['pivot',[30, 250]],
    ['act_run_time',[-700, 250, 'right', 'False']],
    ['gyro_drive',[0, 150, 200, 'True']],
    ['pivot',[-45, 100]],
    ['wait',[150]],
    ['gyro_drive',[0, 150, 400, 'True']],
    ['pivot',[-45, 100]],
    ['wait',[150]],
    ['act_run_time',[-200, 1000, 'right', 'False']],
    ['drive_mm',[0, 75, 140]],
    ['act_run_time',[700, 400, 'right', 'True']],
    ['wait',[100]],
    ['pivot',[20, 100]],
    ['drive_mm',[0, 200, -100]],
    ['pivot',[-90, 100]],
    ['drive_mm',[0, 300, -750]]
  ]
  return commands