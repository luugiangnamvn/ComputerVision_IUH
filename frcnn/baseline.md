# Draft
## introduction
- We are probadly too familiar with the term Computer Vision, it was emerged recently on a few year. Some problems that you may hear or know about are MNIST classification, face mask detection, hand written detection,.. or the lastest idea about a model tracking student to detect cheating. So almost CV tasks is help to detection something to make a decision. Before we dive in our topic research, I will introduce a little bit about our main algrithm that we use in this topic.

## Relevent Knowledge
### Selective Search
- Selective Search is widely used in R-CNN and Fast R-CNN. Selective Search aim to solve the problem object localization.
- Selective Search use sliding window of different size to locate objects in the image. This approach is require very much computation because we need to search a thousands of window even on a small image (about 2000 regions). Selective Search choose some regions proposal base on these characteristics: color similarity, textuture similarity, size similarity, shape similarity, meta-similarity.
### R-CNN
- also know as Region-Convolutional Network. It extracts a bund of regions from the image using selective search, and then checks if any of these boxes contain an object.
![R-CNN architect](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/10/rcnn.png)
- warp image regions to resize image (synchronous input)
- Firstly, we extract all regions, and for each region, CNN is used to extract specific features. Finally, these features are then used to detect objects
- R-CNN is slow because of these multiple steps involved in the process

image --selective_search--> regions proposal + warp image --forward_each-region_through_ConvNet--> bounding boxes
### Fast R-CNN
- Like the name, it is a derivative idea of R-CNN. It still use Selective Search to extract regions proposal but in other way: It will passes the entire image to ConvNet which generates regions of interest (instead of passing the extracted region from the image). Then it use a single model which extracts features from the regions, classifies them into differenct classes and return the bounding boxes
![Fast R-CNN architect](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/10/Fast-rcnn.png)

image --ConvNet--> ROI --selective_search--> regions proposal --ROI_pooling--> regions with same size --FCL--> bounding boxes

### Faster R-CNN
- Faster R-CNN replace Selective Search with a Region Proposal Network to extract regions proposal
![Faster R-CNN architect](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/10/Faster-rcnn.png)
- Firstly, we extract feature maps from the input image using ConvNet and then pass them through a RPN which return objects proposals. Finally, these maps are classified and the bounding boxes are predicted

image --COnvNet--> feature maps --RPN--> objects proposal --> bounding boxes
### transfer leanring
- basically, transfer learning is we used output of a pre-trained model as a input of another model(target tasks), example we use RPN to get regions proposal.


------
references
- https://dlapplications.github.io/2018-07-15-Transfer-Learning-Basic/
- https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/?fbclid=IwAR1KlC1hfSiVJc_RlRwHFFDlSdqcIZBD2rHgzzhn6ik62-nutqH4KrHFxlc
- https://nttuan8.com/bai-11-object-detection-voi-faster-r-cnn/?fbclid=IwAR2cg9hqjth3Dkv0DKei5Morxgj1vJ_6kKeSjRej6HY8Rf4tIdRF6i2NykQ
- https://www.geeksforgeeks.org/selective-search-for-object-detection-r-cnn/
- Faster R-CNN with Region Proposal Refinement (paper on folder)