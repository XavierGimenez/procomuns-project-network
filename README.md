# procomuns-project-network

This visualization has been developed in the context of Visualization and data contest on [_Commons Collaborative Economies: Policies, Technologies and City for the People_](http://procomuns.net/en/), an encounter which aims to highlight the relevance of the commons-oriented approach of peer production and collaborative economy, while proposing public policies and providing technical guidelines to build software platforms for collaborative communities.

The original dataset of the data can be found as a csv file in the [Commons-Based Peer Production directory.](http://directory.p2pvalue.eu/download)

#### Metodology

The aim of the visualization is to highlight how projects are related to each other. In order to do that and since each project has tags assigned to it, connections between projects can be stablished looking at how many tags are shared within projects.

However, there are a lot of projects without assigned tags. To overcome this:

*   We can consider that projects that are tagged can provide an acceptable set of tags which can be reused through all the projects
*   For those projects without tags, look at its description and search for topics from the set of tags. If tag occurrences are found, these tags are linked to the project.
*   With almost all of the projects tagged, an new column is added on the dataset in order to find connections between projects. Two projects are considered as connected when they share a minimum number of tags (3) between them.
*   When the dataset is populated with projects connections, a gdf file is generated in order to have a graph of connected projects.

The graph is managed with [Gephi](https://gephi.org/) in order to stablish a proper layout and set some properties to the nodes. Size of the nodes are proportional to the number of connections of the project and color is related to the type of activity of the project. Finally, a [javascript a GEXF viewer](https://github.com/raphv/gexf-js) is used to release the user interface and provide interactivity to the graph.

Doubts? Questions? contact me at xavi@xavigimenez.net