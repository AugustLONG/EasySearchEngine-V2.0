import org.apache.spark.{SparkContext, SparkConf}
/**
  * Created by LeechanX.
  */

object InvertedIndexBuilder {
  def main(args: Array[String]) {
    val sparkConf = new SparkConf().setAppName("Inverted-Index-Builder")
    val sc = new SparkContext(sparkConf)
    val subInvertedIndexRDD = sc.textFile("hdfs://master:9001/leechanx/searchengine/subInvertedIndex.txt")
    val invertedIndexRDD = subInvertedIndexRDD.map{
      line =>
        val dataArr = line.trim.split("\t")
        val word = dataArr.head
        val wordNodeString = dataArr(1) + "\t" + dataArr(2) + "\t" + dataArr(3)
        (word, wordNodeString)
    }.groupByKey
    invertedIndexRDD.map{ case (word, wordNodeArray) =>
        word + "," + wordNodeArray.size + ":" + wordNodeArray.mkString(";")
    }.saveAsTextFile("hdfs://master:9001/leechanx/searchengine/InvertedIndex")
    sc.stop()
  }
}

