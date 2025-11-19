<div align="center">
  
  # Poisson-Chebyshev
  
  <h4>
    Generate Poisson disk sampling using Chebyshev distance.
  </h4>

</div>

## Demo

insert here

## Description

This implementation generates a Poisson disk sampling on an arbitrary rectangle with a set radius, which represents an average distance between neighbouring points described by the Chebyshev norm (squares instead of circles).

## Installation

By now, move `poisson.py` to your project and use it as a one-file library. PyPi support will be added later.

## User Guide

To generate a sample (a list of pairs of x and y coordinates of the points), simply use the `sample` method from the `poisson` module.

```py
import poisson

RADIUS = 8
MAX_TRIES = 30
WIDTH = 625
HEIGHT = 625

points = poisson.sample(RADIUS, MAX_TRIES, WIDTH, HEIGHT)
```

- RADIUS - approximate distance between points.
- MAX_TRIES - maximum amount of attempts to generate the next active point. As a rule of thumb, 30 is a good value. To increase sampling speed with some losses in accuracy, lower this threshold. 
- WIDTH - width of the rectangle to sample.
- HEIGHT - height of the rectangle to sample.

## Examples

Examples contain:
-  `example_calculate_coverage_graph.py`, which attempts to generate a graph of squares covering the sampled rectangle using an additional parameter of `SQUARE_SIZE`. Generally, the `RADIUS` value varies from `SQUARE_SIZE // 2` for maximum coverage to `SQUARE_SIZE` for minimal overlap. 
- `example_test_radii.py`, which generates a statistic on the ratio of coverage and overlapping by iterating over radii from the range named above.

## Requirements
The library itself does not require any additional imports.

Both examples from the list, however, require `numpy` and the first one requires `matplotlib` as well.