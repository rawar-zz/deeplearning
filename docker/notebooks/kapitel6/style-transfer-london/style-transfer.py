import scipy.misc
import numpy as np
import tensorflow as tf

!wget -O - http://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz > models/vgg16_weights.npz 

from models import vgg
network_model = vgg

C_LAYER = network_model.content_layers()
S_LAYERS = network_model.style_layers()

# layers = dict([(layer.name, layer.output) for layer in model.layers])
# layers
# model.count_params()A

# # Convert it into an array
# x = np.asarray(image, dtype='float32')
# Convert it into a list of arrays
# x = np.expand_dims(x, axis=0)
# Pre-process the input to match the training data
# x = preprocess_input(x)
# preds = model.predict(x)
# print('Predicted:', decode_predictions(preds, top=3)[0])


iterations=1000
content_weight = 1e0
style_weight = 1e3
tv_weight = 0
learning_rate = 1e0

style_image = 'input/style.jpg'
input_image = 'input/content.jpg'




def content_loss(cont_out, target_out, layer, content_weight):
    '''
        # content loss is just the mean square error between the outputs of a given layer
        # in the content image and the target image
    '''
    cont_loss = tf.reduce_sum(tf.square(tf.subtract(target_out[layer], cont_out)))

    # multiply the loss by it's weight
    cont_loss = tf.multiply(cont_loss, content_weight, name="cont_loss")
    #tf.add_to_collection('losses', cont_loss)

    return cont_loss

def get_shape(inp):
    # returns the shape of a tensor or an array
    if type(inp) == type(np.array([])):
        return inp.shape
    else:
        return [i.value for i in inp.get_shape()]

def style_loss(style_out, target_out, layers, style_weight_layer):

    def style_layer_loss(style_out, target_out, layer):
        '''
            # returns the style loss for a given layer between
            # the style image and the target image
        '''
        def gram_matrix(activation):
            flat = tf.reshape(activation, [-1, get_shape(activation)[3]]) # shape[3] is the number of feature maps
            res = tf.matmul(flat, flat, transpose_a=True)
            return res

        N = get_shape(target_out[layer])[3] # number of feature maps
        M = get_shape(target_out[layer])[1] * get_shape(target_out[layer])[2] # dimension of each feature map
        
        # compute the gram matrices of the activations of the given layer
        style_gram = gram_matrix(style_out[layer])
        target_gram = gram_matrix(target_out[layer])

        st_loss = tf.multiply(tf.reduce_sum(tf.square(tf.sub(target_gram, style_gram))), 1./((N**2) * (M**2)))

        # multiply the loss by it's weight
        st_loss = tf.multiply(st_loss, style_weight_layer, name='style_loss')

        #tf.add_to_collection('losses', st_loss)
        return st_loss

    losses = []
    for s_l in layers:
        loss = style_layer_loss(style_out, target_out, s_l)
        losses.append(loss)

    return losses

def total_var_loss(generated, tv_weight):
    ''' 
        Computes the total variation loss of the generated image
    '''
    batch, width, height, channels = get_shape(generated)

    width_var = tf.nn.l2_loss(tf.subtract(generated[:,:width-1,:,:], generated[:,1:,:,:]))
    height_var = tf.nn.l2_loss(tf.subtract(generated[:,:,:height-1,:], generated[:,:,1:,:]))

    return tv_weight*tf.add(width_var, height_var)

# compute layer activations for content
g = tf.Graph()
with g.as_default(), g.device('/cpu:0'), tf.Session() as sess:
    content_pre = np.array([network_model.preprocess(content)])

    image = tf.placeholder('float', shape=content_pre.shape)
    model = network_model.get_model(image)
    content_out = sess.run(model[C_LAYER], feed_dict = {image:content_pre})

# compute layer activations for style
g = tf.Graph()
with g.as_default(), g.device('/cpu:0'), tf.Session() as sess:
    style_pre = np.array([network_model.preprocess(style)])
    image = tf.placeholder('float', shape=style_pre.shape)
    model = network_model.get_model(image)
    style_out = sess.run({s_l:model[s_l] for s_l in S_LAYERS}, feed_dict = {image:style_pre})

# create image merging content and style
saver = tf.train.Saver(...variables...)
g = tf.Graph()
with g.as_default(), g.device('/cpu:0'), tf.Session() as sess:
    # init randomly
    # white noise
    target = tf.random_normal((1,)+content.shape)

    target_pre_var = tf.Variable(target)

    # build model with empty layer activations for generated target image
    model = network_model.get_model(target_pre_var)

    # compute loss
    cont_cost = losses.content_loss(content_out, model, C_LAYER, options.content_weight)
    style_cost = losses.style_loss(style_out, model, S_LAYERS, style_weight_layer)
    tv_cost = losses.total_var_loss(target_pre_var, options.tv_weight)

    total_loss = cont_cost + tf.add_n(style_cost) + tv_cost

    train_step = tf.train.AdamOptimizer(learning_rate).minimize(total_loss)

    sess.run(tf.initialize_all_variables())
    min_loss = float("inf")
    best = None
    for setp in range(iterations):
        train_step.run()
        print('Iteration %d/%d' % (step + 1, iterations))

        if step % 5 == 0:
            saver.save(sess, 'style-model', global_step=step)
            loss = total_loss.eval()
            print('    total loss: %g' % total_loss.eval())
            if(loss < min_loss):
                min_loss = loss
                best = target_pre_var.eval()

    print('  content loss: %g' % cont_cost.eval())
    print('    style loss: %g' % tf.add_n(style_cost).eval())
    print('       tv loss: %g' % tv_cost.eval())
    print('    total loss: %g' % total_loss.eval())


    final = best
    final = final.squeeze()
    final = network_model.postprocess(final)

    final = np.clip(final, 0, 255).astype(np.uint8)

    scipy.misc.imsave(out, final)
