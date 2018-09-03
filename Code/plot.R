folder="C:/Users/chili83/Desktop/Distributed Systems/Results"


path<-paste(folder,"resLookUp.csv",sep="/")
data<-read.csv(path,header=FALSE,stringsAsFactors = FALSE)

rows.append<-function(index){
  for(i in index){
    if(i==index[1]){
      rows=c(as.numeric(data[index[1],-1]))
    }else{
      rows=c(rows,as.numeric(data[i,]))
    }
  } 
  return(rows)
}

rows.nor=list(as.numeric(data[1,-1]),as.numeric(data[2,-1]),as.numeric(data[3,-1]),as.numeric(data[4,-1]),as.numeric(data[5,-1]))
rows.abnor=c(as.numeric(data[6,-1]),as.numeric(data[7,]))
rows.nor[[6]]=rows.abnor
rows.abnor=c(as.numeric(data[8,-1]),as.numeric(data[9,]),as.numeric(data[10,]),as.numeric(data[11,]))
rows.nor[[7]]=rows.abnor

index=c(12:(12+8-1))
rows.abnor=rows.append(index)
rows.nor[[8]]=rows.abnor

index=c(20:(20+16-1))
rows.abnor=rows.append(index)
rows.nor[[9]]=rows.abnor

index=c(36:(36+32-1))
rows.abnor=rows.append(index)
rows.nor[[10]]=rows.abnor

index=c(68:(68+64-1))
rows.abnor=rows.append(index)
rows.nor[[11]]=rows.abnor

index=c(132:(132+128-1))
rows.abnor=rows.append(index)
rows.nor[[12]]=rows.abnor

res.insert=lapply(rows.nor,quantile,c(.01,.5,.99),na.rm = TRUE)

boxplot(res.insert,names=c(3:14),xlab="k",ylab="path length")
x=c(3:14)
y=0.5*log2(2**x)
lines(y,col="red")

path<-paste(folder,"resInsertion.csv.bak",sep="/")
data<-read.csv(path,header=FALSE,stringsAsFactors = FALSE)
rows.nor=list(as.numeric(data[1,-1]),as.numeric(data[2,-1]),as.numeric(data[3,-1]),as.numeric(data[4,-1]),as.numeric(data[5,-1]),as.numeric(data[6,-1]),as.numeric(data[7,-1]),as.numeric(data[8,-1]),as.numeric(data[9,-1]),as.numeric(data[10,-1]),as.numeric(data[11,-1]),as.numeric(data[12,-1]))
res.insert=lapply(rows.nor,quantile,c(.01,.5,.99),na.rm = TRUE)

path<-paste(folder,"resInsertion.csv",sep="/")
data<-read.csv(path,header=FALSE,stringsAsFactors = FALSE)
rows.nor=list(as.numeric(data[1,-1]),as.numeric(data[2,-1]),as.numeric(data[3,-1]),as.numeric(data[4,-1]),as.numeric(data[5,-1]),as.numeric(data[6,-1]),as.numeric(data[7,-1]),as.numeric(data[8,-1]),as.numeric(data[9,-1]),as.numeric(data[10,-1]),as.numeric(data[11,-1]),as.numeric(data[12,-1]))
res.insert2=lapply(rows.nor,quantile,c(.01,.5,.99),na.rm = TRUE)
boxplot(res.insert2, names=c(3:14),xlab="k",ylab="path length", col="grey")

x=c(3:14)
y=4.5*(log2(2**x))**2+200
lines(y,col="red")

#x=c(3:14)
#y=130*log2(2**x)
#lines(y,col="red")

# x=c(3:14)
# y=250*log2(log2(2**x))
# lines(y,col="grey")