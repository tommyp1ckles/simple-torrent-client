import libtorrent
import time
import sys

ses = libtorrent.session()
ses.listen_on(6881, 6891)
tracker_type = sys.argv[1]

torrent_info = libtorrent.torrent_info(sys.argv[1])
savepath = './'
params = {'ti' : torrent_info, 'save_path': savepath}
if sys.argv[1] is "--magnet":
	params = {'ti' : torrent_info, 'save_path': savepath}
	link = sys.argv[2]
	handle = libtorrent.add_magnet_uri(ses, link, params)
else:
	torrent_info = libtorrent.torrent_info(sys.argv[1])
	t = ses.add_torrent(params)
print "starting", t.name()
print '\n'

while (not t.is_seed()):
	s = t.status()
	tstates = ['queued', 'checking', 'downloading metadata', 'downloading', \
		'finished', 'seeding', 'allocating', 'checking fastresume']
	
	print 'Completed', s.progress * 100
	print ' | Down speed:', s.download_rate / 1000
	print ' | Up speed:', s.upload_rate / 1000
	print ' | Peers:', s.num_peers
	print ' | state:', tstates[s.state]
	print '\n'
	sys.stdout.flush()

	time.sleep(1)

print t.name(), 'complete'
