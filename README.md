#### A fun GAN exploration!

- GAN implementation using Tensorflow / Keras, based on CycleGAN architecture, designed to transform landscape photos into animations
- Landscape photos were collected from flickr, animated photos were collected using python, scenedetect and Studio Ghibli trailers / compilation videos found on YouTube

**Results:**

- After around 65+ epochs of training, losses converged to an equilibrium of around:

```
d1[0.002,0.028] d2[0.073,0.035] g[2.486,3.182]
```

- (Discriminator 1, 2, and generator losses, respectively.)

**After ~65 epochs:**

![0](./results/0.png)

![5](./results/1.png)

![4](./results/3.png)

![5](./results/5.png)

**Early results - after ~20 epochs:**

![0](./results/early_0.png)

![4](./results/early_1.png)

![5](./results/early_5.png)