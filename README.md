# opensource4medicine
Open source programs useful in medicine. Also check the repositories for Debora and Neuromath of mine: those are primitive, but innovative in terms of how I look at histogram bins.
I am in the process of adding lisences to everything, but the basic idea, is that you can use any of it, but you need to send back the new code you made- and credit me in any related research.

The program readthestackcommandline will let you read through a bunch of texts (I would presume some kind of reports) and search for words you input. An example of use would be if you had 500 radiology reports and you wanted to find the ones wwhere the text "pancreatitis" or "cholangitis appeared." 

Some of the programs in this repository that refer to the University of Indiana Chest Xray set (i.e. uoficlassifynormalwritecsv2xl, popoutstringfromuofi 	and	uofindianacxrayclassifynormal) use data in this set for training data. The data can be downloaded off the internet at:
Documents: http://academictorrents.com/details/66450ba52ba3f83fbf82ef9c91f2bde0e845aba9
Images: http://academictorrents.com/details/5a3a439df24931f410fac269b87b050203d9467d
Note that programs using higher levels of NLP are now the property of Ikhami. NLP available in UofIani folder does not handle specific complex strings such as""resolution of previously described right midlung opacity", "resolution of previosly described opacity" as strings upon which to classify Xrays as it is possible to have a report that has a resolving opacitty in one area and the appearance of a new opacity in another. This level of complex NLP will be available through Ikhami in potentially commercial products. 

Automated augmented data program was made using U of I CXR set as well- but  submodoles are applicable to any Xrays, as far as I can tell.
