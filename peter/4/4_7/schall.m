c=337.5;
n=50;

vv=[0.5*c,c,2*c];

for iv=1:3
    v=vv(iv);
    t=linspace(0,1,50);    
    Mx=v.*t;
    My = zeros(size(Mx));
    r=c.*fliplr(t);    
    figure(iv);
    hold on;
    for ii=1:length(t)
        [x,y]=kreisf1(Mx(ii),My(ii),r(ii),n);
        plot(x,y,'k');
    end
    plot(Mx,My,'r*');
    axis equal;
    axis off;
    title(['v = ',num2str(v), ' m/s']);
end
hold off;