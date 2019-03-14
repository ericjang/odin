from __future__ import division
from __future__ import print_function
import os
def main():
  with open("list_eval_partition.txt", "r") as f:
    for line in f.readlines():
      name, split = line.split(" ")
      if split[0] == '2':
        # test set
        print(name)
        os.rename("img_align_celeba/%s" % name, "test/%s" % name)


if __name__ == '__main__':
  main()
