import handin5
import matplotlib.pyplot as plt
larger_than_neighbor_count = handin5.count_larger_than_neighbor_without_loops([6,9,4,8,7,1,2])
print(larger_than_neighbor_count)

#verify q2

mnist_data = handin5.read_mnist_csv("mnist_test_200.csv")
print(mnist_data)
print("\n")
print("Mnisdata shapr", mnist_data.shape)
print("\n")
#q3
digit_image_groups = handin5.group_by_label(mnist_data)
#import pdb;pdb.set_trace()
print(digit_image_groups)


#question 4
digit_image = handin5.get_image(digit_image_groups,0)
print(digit_image)
print(digit_image.shape)
plt.imshow(digit_image, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.savefig("random_image.png")
plt.show()




