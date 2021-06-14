import vpython as vp

R_STALK_0 = 0.7
R_STALK_1 = 2


def draw_root(id: str, length: float, x: float, y: float):
    color = vp.color.orange
    texture = vp.textures.granite

    if id == '0':
        vp.cylinder(pos=vp.vector(x, y, 0), axis=vp.vector(0, -length, 0), radius=0.4, color=color, texture=texture)
        vp.cone(pos=vp.vector(x, y-length, 0), axis=vp.vector(0, -1, 0), radius=0.4, color=color, texture=texture)

    if id == '1':
        c = vp.curve(color=color, radius=0.15)
        c1 = vp.curve(color=color, radius=0.15)
        c2 = vp.curve(color=color, radius=0.15)
        c3 = vp.curve(color=color, radius=0.15)
        cr = vp.curve(color=color, radius=0.2)

        v1 = vp.vector(x, y, 0)
        cr.append(v1, vp.vector(x,y-2,0))

        v2 = vp.vector(x+1, y-0.6, 0)
        v3 = vp.vector(x+length, y-2, 0)
        c.append(v1, v2, v3)

        v2 = vp.vector(x - 1, y - 0.6, 0)
        v3 = vp.vector(x - length, y - 2, 0)
        c1.append(v1, v2, v3)

        v2 = vp.vector(x, y - 0.5, 1)
        v3 = vp.vector(x, y - 2, length)
        c2.append(v1, v2, v3)

        v2 = vp.vector(x, y - 0.5, -1)
        v3 = vp.vector(x, y - 2, -length)
        c3.append(v1, v2, v3)


def draw_stalk(typ_id: str, creation_id: str, length: float, x: float, y: float):
    sfe = None
    color = vp.color.green

    if typ_id == '0':
        stalk = vp.cylinder(pos=vp.vector(x, y, 0), axis=vp.vector(0, length, 0), radius=R_STALK_0)
    if typ_id == '1':
        stalk = vp.cylinder(pos=vp.vector(x, y, 0), axis=vp.vector(0, length, 0), radius=R_STALK_1)
        sfe = vp.sphere(pos=vp.vector(x, y+length, 0), radius=R_STALK_1, axis=vp.vector(0, 2, 0), up=vp.vector(0, 0, -1))

    if creation_id =='00':
        #skórka
        texture = vp.textures.stucco
        #color = vp.color.blue
    if creation_id == '01':
        #wosk
        texture = vp.textures.metal
        #color = vp.color.yellow
    if creation_id == '10':
        #kora
        texture = vp.textures.rock
        color = vp.color.orange
    if creation_id == '11':
        color = vp.color.green
        texture = None
    stalk.color = color
    stalk.texture = texture
    if sfe:
        sfe.color = color
        sfe.texture = texture


def draw_leaves(typ_id:str, color_id:str, stalk_type: str, length: float, x:float, y:float):
    r = 0
    if stalk_type == '0': r = R_STALK_0
    if stalk_type == '1': r = R_STALK_1

    color = None
    if color_id == '00':
        color = vp.color.green
    if color_id == '01':
        color = vp.color.orange
    if color_id == '10':
        color = vp.color.red
    if color_id == '11':
        color = vp.color.purple


    if typ_id == '00':
        # małe
        draw_small_ls(length, color, x, y, r)

    if typ_id == '01':
        # duże
        draw_big_ls(length, color, x, y, r)

    if typ_id == '10':
        # miesiste
        draw_meat_ls(length, color, x, y, r)

    if typ_id == '11':
        #kolce
        draw_thorns(length, color, x, y, r)


def draw_thorns(length: float, color, x, y, r):
    color = vp.color.black
    y -= 0.5
    between_leaves = 2
    leaf_length = 0.5
    count = int(length / between_leaves) + 1

    for i in range(1, count):
        vp.cone(pos=vp.vector(x+r, y + (i * between_leaves)-1, 0), axis=vp.vector(leaf_length, 0, 0), radius=0.1, color=color)
    for i in range(1, count):
        vp.cone(pos=vp.vector(x-r, y + (i * between_leaves)-1, 0), axis=vp.vector(-leaf_length, 0, 0), radius=0.1, color=color)
    for i in range(1, count):
        vp.cone(pos=vp.vector(x, y + (i * between_leaves), r), axis=vp.vector(0, 0, leaf_length), radius=0.1, color=color)
    for i in range(1, count):
        vp.cone(pos=vp.vector(x, y + (i * between_leaves), -r), axis=vp.vector(0, 0, -leaf_length), radius=0.1, color=color)


def draw_small_ls(length: float, color, x, y, r):
    y -= 0.5
    between_leaves = 2
    leaf_len = 0.7
    leaf_hei = 0.1
    leaf_wid = 0.5
    down =0.2
    count = int(length / between_leaves) + 1

    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x+r+0.2, y+(i * between_leaves)-0.5, 0), up=vp.vector(0.2, down, 0)
                     , length=leaf_len, height=leaf_hei, width=leaf_wid, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x-r-0.2, y + (i * between_leaves)-0.5, 0), up=vp.vector(-0.2, down, 0)
                     , length=leaf_len, height=leaf_hei, width=leaf_wid, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x, y+(i * between_leaves), r+0.2), up=vp.vector(0, down, 0.2)
                     , length=leaf_wid, height=leaf_hei, width=leaf_len, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x, y + (i * between_leaves), -r-0.2), up=vp.vector(0, down, -0.2)
                     , length=leaf_wid, height=leaf_hei, width=leaf_len, color=color)


def draw_big_ls(length: float, color, x, y, r):
    y -= 0.5
    between_leaves = 2
    leaf_len = 2
    leaf_hei = 0.3
    leaf_wid = 1.7
    down = 0.1
    count = int(length / between_leaves) + 1

    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x + r + 0.2, y + (i * between_leaves) - 0.5, 0), up=vp.vector(0.2, down, 0)
                     , length=leaf_len, height=leaf_hei, width=leaf_wid, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x - r - 0.2, y + (i * between_leaves) - 0.5, 0), up=vp.vector(-0.2, down, 0)
                     , length=leaf_len, height=leaf_hei, width=leaf_wid, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x, y + (i * between_leaves), r + 0.2), up=vp.vector(0, down, 0.2)
                     , length=leaf_wid, height=leaf_hei, width=leaf_len, color=color)
    for i in range(1, count):
        vp.ellipsoid(pos=vp.vector(x, y + (i * between_leaves), -r - 0.2), up=vp.vector(0, down, -0.2)
                     , length=leaf_wid, height=leaf_hei, width=leaf_len, color=color)

def draw_meat_ls(length: float, color, x, y, r):
    y -= 0.5
    between_leaves = 3
    count = int(length / between_leaves) + 1
    rad = 0.5
    d = 0.3

    for i in range(1, count):
        vp.sphere(pos=vp.vector(x+r+d, y+(i*between_leaves)-0.5, 0), radius=rad, color=color)
    for i in range(1, count):
        vp.sphere(pos=vp.vector(x-r-d, y+(i*between_leaves)-0.5, 0), radius=rad, color=color)
    for i in range(1, count):
        vp.sphere(pos=vp.vector(x, y+(i*between_leaves), r+d), radius=rad, color=color)
    for i in range(1, count):
        vp.sphere(pos=vp.vector(x, y+(i * between_leaves), -r-d), radius=rad, color=color)
