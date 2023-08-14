import arcade
import numpy as np
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Animaciones 2D"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size=10
        self.estadoAnimacion=0
        self.speed=10

    def on_draw(self):
        arcade.start_render()
        vertices = [(100,100),(100,200),(200,200),(200,100)]
        arcade.draw_polygon_outline(vertices,arcade.color.YELLOW,5)
        new_vertices=self.translate2(vertices,200,200)
        arcade.draw_polygon_outline(new_vertices,arcade.color.GO_GREEN,5)
        new_vertices2=self.rotate2(vertices,self.estadoAnimacion)
        

        arcade.draw_polygon_outline(new_vertices2,arcade.color.RED,5)
        new_vertices3=self.scale2(vertices,200,200)
        arcade.draw_polygon_outline(new_vertices3,arcade.color.GO_GREEN,5)

    
    def translate(self,vertices,dx,dy):
        new_vertices = [(v[0]+dx,v[1]+dy)for v in vertices]
        return new_vertices
    
    def rotate(self,vertices, theta):
        TM=np.array([[np.cos(theta),-np.sin(theta),0],
                     [np.sin(theta),np.cos(theta),0],
                     [0,0,1]])
        return self.apply_tr_matrix(vertices,TM)
    
    def scale(self,vertices, sx, sy):
        TM=np.array([[sx,0,0],
                     [0,sy,0],
                     [0,0,1]])
        return self.apply_tr_matrix(vertices,TM)
    
    #version correcta de implementación
    def translate2(self,vertices,dx,dy):
        TM=np.array([[1,0,dx],
                     [0,1,dy],
                     [0,0,1]])
        
        return self.apply_tr_matrix(vertices,TM)
    
    def rotate2(self, vertices,theta):
        xc,yc = self.get_center(vertices)
        Mt1=np.array([[1,0,-xc],
                     [0,1,-yc],
                     [0,0,1]])
        
        Mr=np.array([[np.cos(theta),-np.sin(theta),0],
                     [np.sin(theta),np.cos(theta),0],
                     [0,0,1]])
        
        Mt2=np.array([[1,0,xc],
                     [0,1,yc],
                     [0,0,1]])
        
        TM = np.dot(Mt2,np.dot(Mr,Mt1))
        return self.apply_tr_matrix(vertices,TM)
    
    def scale2(self,vertices, sx, sy):
        xc,yc = self.get_center(vertices)
        Mt1=np.array([[1,0,-xc],
                     [0,1,-yc],
                     [0,0,1]])
        
        Ms=np.array([[sx,0,0],
                     [0,sy,0],
                     [0,0,1]])
        
        Mt2=np.array([[1,0,xc],
                     [0,1,yc],
                     [0,0,1]])
        
        TM = np.dot(Mt2,np.dot(Ms,Mt1))
        return self.apply_tr_matrix(vertices,TM)
    
    def apply_tr_matrix(self,vertices,tr_matrix):
        v_array = np.array([[v[0],v[1],1]for v in vertices])
        v_array=np.transpose(v_array)
        #aplicar transformacion
        new_vertices_array=np.dot(tr_matrix,v_array)
        new_vertices=np.transpose(new_vertices_array[0:2,:])
        new_vertices=new_vertices.tolist()
        return new_vertices
    
    def get_center(self,vertices):
        return np.mean(np.array(vertices),axis=0)



    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [20, 20, 20]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [20, 20, 20]
            )

    def on_update(self,delta_time:float):
        self.estadoAnimacion+=delta_time*self.speed

        self.on_draw()

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()