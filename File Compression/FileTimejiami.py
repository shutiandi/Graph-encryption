timdatemax=24-1
timdtx=60-1
timddx=60-1
stmon=12+12-1
stmonlist=[31,28,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31]#非闰年影响时间，即每有具体年份信息
stmonlistnums=[2678400,5097600,7776000,10368000,13046400,15638400,18316800,20995200,23587200,26265600,28857600,31536000,34214400,36720000,39398400,41990400,44668800,47260800,49939200,52617600,55209600,57888000,60480000,63158400]
stm=0
std=0
ttm=0
tt=0
td=0
def filetimer(filename,newfilename):
  filered=open(filename,mode="rb")
  filewr=open(newfilename,mode="wb")
  while True:
    stwd=filered.read(5)
    if len(stwd) !=5:
        filewr.write(stwd)
        break
    td+=1
    if td==60:
        td=0
        tt+=1
    if tt==60:
        tt=0
        ttm+=1
    if ttm==24:
        ttm=0
        std+=1
    if std==stmonlist[stm]:
        std=0
        stm+=1
    if stm==24:
        stm=0

    wd,wt,wtm,wstd,wstm=(td+stwd[0])%256,(tt+stwd[1])%256,(ttm+stwd[2])%256,(std+stwd[3])%256,(stm+stwd[4])%256
    filewr.write(int(wd).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wt).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wtm).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wstd).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wstm).to_bytes(length=1,byteorder="little"))
  filewr.close()
  filered.close()
def refiletimer(filename,newfilename):
    filered=open(filename,mode="rb")
  filewr=open(newfilename,mode="wb")
  while True:
    stwd=filered.read(5)
    if len(stwd) !=5:
        filewr.write(stwd)
        break
    td+=1
    if td==60:
        td=0
        tt+=1
    if tt==60:
        tt=0
        ttm+=1
    if ttm==24:
        ttm=0
        std+=1
    if std==stmonlist[stm]:
        std=0
        stm+=1
    if stm==24:
        stm=0

    wd,wt,wtm,wstd,wstm=(stwd[0]-td+256)%256,(stwd[1]-tt+256)%256,(stwd[2]-ttm+256)%256,(stwd[3]-std+256)%256,(stwd[4]-stm+256)%256
    filewr.write(int(wd).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wt).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wtm).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wstd).to_bytes(length=1,byteorder="little"))
    filewr.write(int(wstm).to_bytes(length=1,byteorder="little"))
  filewr.close()
  filered.close()

