from load import graph
from draw import draw


def main():
    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())

    degree_dict = dict(graph.degree())

    sorted_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)

    # Display the top 5 nodes by degree
    top_nodes = sorted_nodes[:5]
    print("\nTop 5 nodes by degree:")
    for node, degree in top_nodes:
        print(f"{node}: {degree}")

    draw(graph, title='Les Miserables characters interaction')


if __name__ == '__main__':
    main()
